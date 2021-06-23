from config import app

from news_views import *
from error_views import *
from admin_news_views import *
from context import *


if __name__ == "__main__":
    app.run(debug=True)