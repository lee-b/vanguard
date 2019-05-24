from .app import app
from .entries import *


def main():
    app.run(debug=True)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())