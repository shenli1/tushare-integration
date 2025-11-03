import datetime
import typer

from tushare_integration.commands import crawl_app, query_app

app = typer.Typer(name='CrawlManager', help='CrawlManager help', no_args_is_help=True)


def is_weekday():
    """判断今天是否是工作日（周一到周五）"""
    today = datetime.datetime.now().weekday()
    # 周一到周五是工作日，返回True
    return today < 5


def main():
    # 如果没有提供任何参数，则根据当前日期自动选择运行哪个job
    import sys
    if len(sys.argv) == 1:  # 只有脚本名，没有其他参数
        if is_weekday():
            print("今天是工作日，自动运行daily job")
            sys.argv.extend(["run", "job", "daily"])
        else:
            print("今天是周末，自动运行all job")
            sys.argv.extend(["run", "job", "all"])
    
    app.add_typer(crawl_app, name='run')
    app.add_typer(query_app, name='query')

    app()


if __name__ == '__main__':
    main()
