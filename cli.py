import click
from aiohttp import web
from app import create_app


@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=8080)
def main(host, port):
    app = create_app()
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
