import importlib
import pkgutil

from app import routes

def register_routes(app):

    for module_info in pkgutil.iter_modules(routes.__path__):

        module_name = module_info.name

        if module_name == "__init__":
            continue

        module = importlib.import_module(
            f"app.routes.{module_name}"
        )

        for name in dir(module):

            obj = getattr(module, name)

            if name.endswith("_bp"):
                app.register_blueprint(obj)