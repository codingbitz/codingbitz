from pkgtt import create_app
import os
config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='127.0.0.5', port=5000, debug=True)
