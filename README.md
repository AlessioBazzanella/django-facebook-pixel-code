django-facebook-pixel-code
==========================

Template tag to install your Facebook Pixel Code account in your
templates (https://www.facebook.com/business/help/www/651294705016616/)

## Installation and Usage

1. run `pip install django-facebook-pixel-code`
2. add `'facebook_pixel_code'` to your `INSTALLED_APPS` setting.
3. set `FACEBOOK_PIXEL_CODE_ID` to your Facebook Pixel Code Id.
4. In your templates (probably in your base template) you `{% load
   fpc_tags %}` and then `{% fpc %}` between the `<head>` and `</head>`
   tags.
5. Profit
