#!/usr/bin/env python3

import os

import uvicorn

from .app import create_app


def main():
    """Entry point for testing or simple deployment."""

    app = create_app()
    uvicorn.run(app,
                host=os.environ.get('HOST', '::'),
                port=int(os.environ.get('PORT', 8000)),
                use_colors=True,
                debug=True)


if __name__ == "__main__":
    main()
