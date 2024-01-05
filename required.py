from flask import redirect, url_for


def redirect_user(source,target):
    if source == target:
        return True
    else:
        return False