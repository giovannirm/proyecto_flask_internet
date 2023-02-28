# from flask import Blueprint, redirect, url_for, request
# from src.models.todo import Todo
# from src.db import db

# post = Blueprint('post', __name__)

# @post.route("/add", methods=["POST"])
# def add():
#     title = request.form.get("title")
#     new_todo = Todo(title=title, complete=False)
#     db.session.add(new_todo)
#     db.session.commit()
#     return redirect(url_for("get.home"))