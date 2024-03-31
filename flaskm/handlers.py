from flask import render_template, Blueprint


bp = Blueprint("users", __name__, url_prefix="")


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/list_prof/<marker>")
def list_prof(marker):
    profs = ['Профессия 1', 'Профессия 2', 'Профессия 3', 'Профессия 4', 'Профессия 5',
     'Профессия 6', 'Профессия 7', 'Профессия 8', 'Профессия 9', 'Профессия 10',
     'Профессия 11', 'Профессия 12', 'Профессия 13', 'Профессия 14', 'Профессия 15']
    return render_template("list_prof.html", profs=profs, marker=marker)
