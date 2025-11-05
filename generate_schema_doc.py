#!/usr/bin/env python3
"""
生成数据库说明书
扫描所有 schema YAML 文件并生成完整的数据库文档
"""
import pathlib
import yaml
from typing import Dict, List, Any
from datetime import datetime


def load_schema_file(file_path: pathlib.Path) -> Dict[str, Any]:
    """加载 YAML schema 文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f.read())


def get_data_type_desc(data_type: str, length: int) -> str:
    """获取数据类型的完整描述"""
    if data_type == 'str':
        if length > 0:
            return f"VARCHAR({length})"
        else:
            return "TEXT"
    elif data_type == 'int':
        return "INTEGER"
    elif data_type == 'float':
        return "DOUBLE"
    elif data_type == 'date':
        return "DATE"
    elif data_type == 'datetime':
        return "DATETIME"
    else:
        return data_type.upper()


def generate_table_doc(schema: Dict[str, Any], schema_path: str) -> str:
    """生成单个表的文档"""
    lines = []
    
    # 表基本信息 - 压缩在一行内，不换行
    table_info_parts = []
    table_info_parts.append(f"**表名**: `{schema.get('name', 'unknown')}`")
    table_info_parts.append(f"**说明**: {schema.get('comment', '无说明')}")
    
    # 主键
    primary_key = schema.get('primary_key', [])
    if primary_key:
        table_info_parts.append(f"**主键**: {', '.join([f'`{pk}`' for pk in primary_key])}")
    
    # 依赖关系
    dependencies = schema.get('dependencies', [])
    if dependencies:
        table_info_parts.append(f"**依赖表**: {', '.join([f'`{dep}`' for dep in dependencies])}")
    
    # 索引
    indexes = schema.get('indexes', [])
    if indexes:
        table_info_parts.append(f"**索引**: {', '.join([f'`{idx}`' for idx in indexes])}")
    
    lines.append(f"### {schema.get('name', 'unknown')}")
    lines.append("")
    lines.append(" | ".join(table_info_parts))
    lines.append("")
    
    # 字段列表
    lines.append("**字段列表**:")
    lines.append("")
    lines.append("| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |")
    lines.append("|--------|----------|------|--------|------|")
    
    columns = schema.get('columns', [])
    for col in columns:
        name = col.get('name', '')
        data_type = get_data_type_desc(col.get('data_type', 'str'), col.get('length', 0))
        length = col.get('length', 0) if col.get('data_type') == 'str' else '-'
        default = col.get('default', '')
        comment = col.get('comment', '无说明') or '无说明'
        # 处理多行注释
        comment = comment.replace('\n', ' ').replace('|', '\\|')
        lines.append(f"| `{name}` | {data_type} | {length} | `{default}` | {comment} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    return "\n".join(lines)


def generate_database_doc() -> str:
    """生成完整的数据库文档"""
    schema_dir = pathlib.Path(__file__).parent / 'tushare_integration' / 'schema'
    
    # 按分类组织
    categories = {
        '股票-基础信息': [],
        '股票-财务数据': [],
        '股票-行情数据': [],
        '股票-市场数据': [],
        '股票-资金流向': [],
        '股票-融资融券': [],
        '股票-涨跌停': [],
        '股票-特殊数据': [],
        '指数-基础信息': [],
        '指数-行情数据': [],
        '指数-SW分类': [],
        '指数-同花顺': [],
        '指数-中信': [],
        '期货-基础信息': [],
        '期货-行情数据': [],
    }
    
    # 扫描所有 YAML 文件
    schema_files = sorted(schema_dir.rglob('*.yaml'))
    
    for schema_file in schema_files:
        relative_path = schema_file.relative_to(schema_dir.parent)
        schema_path = str(relative_path).replace('\\', '/').replace('.yaml', '')
        
        try:
            schema = load_schema_file(schema_file)
            
            # 根据路径分类
            path_str = str(schema_file.relative_to(schema_dir))
            if path_str.startswith('stock/basic/'):
                categories['股票-基础信息'].append((schema_path, schema))
            elif path_str.startswith('stock/financial/'):
                categories['股票-财务数据'].append((schema_path, schema))
            elif path_str.startswith('stock/quotes/'):
                categories['股票-行情数据'].append((schema_path, schema))
            elif path_str.startswith('stock/market/'):
                categories['股票-市场数据'].append((schema_path, schema))
            elif path_str.startswith('stock/moneyflow/'):
                categories['股票-资金流向'].append((schema_path, schema))
            elif path_str.startswith('stock/margin/'):
                categories['股票-融资融券'].append((schema_path, schema))
            elif path_str.startswith('stock/limit/'):
                categories['股票-涨跌停'].append((schema_path, schema))
            elif path_str.startswith('stock/special/'):
                categories['股票-特殊数据'].append((schema_path, schema))
            elif path_str.startswith('index/basic/'):
                categories['指数-基础信息'].append((schema_path, schema))
            elif path_str.startswith('index/quotes/'):
                categories['指数-行情数据'].append((schema_path, schema))
            elif path_str.startswith('index/sw/'):
                categories['指数-SW分类'].append((schema_path, schema))
            elif path_str.startswith('index/ths/'):
                categories['指数-同花顺'].append((schema_path, schema))
            elif path_str.startswith('index/zx/'):
                categories['指数-中信'].append((schema_path, schema))
            elif path_str.startswith('future/basic/'):
                categories['期货-基础信息'].append((schema_path, schema))
            elif path_str.startswith('future/quotes/'):
                categories['期货-行情数据'].append((schema_path, schema))
            else:
                # 未知分类，添加到其他
                if '其他' not in categories:
                    categories['其他'] = []
                categories['其他'].append((schema_path, schema))
        except Exception as e:
            print(f"Error loading {schema_file}: {e}")
    
    # 生成文档
    doc_lines = []
    doc_lines.append("# Tushare Integration 数据库说明书")
    doc_lines.append("")
    doc_lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    doc_lines.append("")
    doc_lines.append("## 目录")
    doc_lines.append("")
    
    # 生成目录
    for category in categories.keys():
        if categories[category]:
            anchor = category.replace(' ', '-').lower()
            doc_lines.append(f"- [{category}](#{anchor})")
    
    doc_lines.append("")
    doc_lines.append("---")
    doc_lines.append("")
    
    # 生成各分类内容
    total_tables = 0
    for category, tables in categories.items():
        if not tables:
            continue
        
        total_tables += len(tables)
        anchor = category.replace(' ', '-').lower()
        doc_lines.append(f"## {category} {{#{anchor}}}")
        doc_lines.append("")
        doc_lines.append(f"本分类共包含 **{len(tables)}** 个数据表。")
        doc_lines.append("")
        
        # 生成表列表
        doc_lines.append("### 表列表")
        doc_lines.append("")
        for schema_path, schema in sorted(tables, key=lambda x: x[1].get('id', 0)):
            table_name = schema.get('name', 'unknown')
            comment = schema.get('comment', '无说明')
            doc_lines.append(f"- [{table_name}](#{table_name.lower().replace('_', '-')}) - {comment}")
        
        doc_lines.append("")
        
        # 生成每个表的详细文档
        for schema_path, schema in sorted(tables, key=lambda x: x[1].get('id', 0)):
            doc_lines.append(generate_table_doc(schema, schema_path))
    
    doc_lines.append("## 统计信息")
    doc_lines.append("")
    doc_lines.append(f"- **总表数**: {total_tables}")
    doc_lines.append(f"- **生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    doc_lines.append("")
    
    return "\n".join(doc_lines)


def main():
    """主函数"""
    print("正在生成数据库说明书...")
    doc = generate_database_doc()
    
    output_file = pathlib.Path(__file__).parent / 'docs' / 'database_schema.md'
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(doc)
    
    print(f"数据库说明书已生成: {output_file}")
    print(f"文档大小: {len(doc)} 字符")


if __name__ == '__main__':
    main()

