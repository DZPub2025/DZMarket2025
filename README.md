# DzMarket - Backend Starter

This is a minimal Django + DRF starter for DzMarket (mobile + backend).

## Quickstart (dev)
1. Create virtualenv: `python -m venv venv && source venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Run server: `python manage.py runserver`

Notes:
- Settings use SQLite by default for development.
- Configure Cloudinary via environment variables for image hosting.


## Image upload endpoints
You can upload ad images via the backend at `POST /api/ads/<ad_id>/images/` (multipart field `image`) or provide `image_url` in JSON. Only the ad's seller may add/delete images.

