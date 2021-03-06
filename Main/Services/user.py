from Main.Models.User import User


def login_user(form):
    users = User.objects.all()

    if form.is_valid():
        username = form['username'].value()

        for user in users:
            if user.username == username:
                return user.id

    return 0


def create_user(form):
    user = User()
    if form.is_valid():
        user.username = form['username'].value()

        user.save()


def read_all_user():
    users = User.objects.all()

    return users


def read_user(pk):
    user = User.objects.get(id=pk)
    return user


def update_user(form, pk):
    user = User.objects.get(id=pk)
    if form.is_valid():
        user.username = form['username'].value()

        user.save()


def delete_user(pk):
    user = read_user(pk)

    user.delete()
