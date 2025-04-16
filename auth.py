import os
import json

class User:
    def __init__(self, username):
        self.username = username
        self.role = self.get_role()

    def get_role(self):
        with open("users.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == self.username:
                    return data[-1]  # last field is role
        return None

    def get_profile(self):
        with open("users.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == self.username:
                    return {
                        "id": data[0],
                        "name": data[1],
                        "email": data[2],
                        "role": data[3]
                    }
        return None

    def view_grades(self):
        try:
            with open("grades.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == self.username:
                        return list(map(int, data[1:]))
        except FileNotFoundError:
            return []
        return []

    def view_eca(self):
        try:
            with open("eca.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == self.username:
                        return data[1:]
        except FileNotFoundError:
            return []
        return []

    def update_profile(self, new_name, new_email):
        updated = []
        with open("users.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            data = line.strip().split(",")
            if data[0] == self.username:
                data[1] = new_name
                data[2] = new_email
            updated.append(",".join(data))
        with open("users.txt", "w") as f:
            f.write("\n".join(updated) + "\n")


class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def add_user(self, user_id, name, email, role, password):
        with open("users.txt", "a") as f:
            f.write(f"{user_id},{name},{email},{role}\n")
        with open("passwords.txt", "a") as f:
            f.write(f"{user_id},{password}\n")

    def update_grades(self, user_id, grades):
        updated = []
        found = False
        with open("grades.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            data = line.strip().split(",")
            if data[0] == user_id:
                data = [user_id] + list(map(str, grades))
                found = True
            updated.append(",".join(data))
        if not found:
            updated.append(",".join([user_id] + list(map(str, grades))))
        with open("grades.txt", "w") as f:
            f.write("\n".join(updated) + "\n")

    def update_eca(self, user_id, activities):
        updated = []
        found = False
        with open("eca.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            data = line.strip().split(",")
            if data[0] == user_id:
                data = [user_id] + activities
                found = True
            updated.append(",".join(data))
        if not found:
            updated.append(",".join([user_id] + activities))
        with open("eca.txt", "w") as f:
            f.write("\n".join(updated) + "\n")

    def delete_user(self, user_id):
        def filter_out(filepath):
            with open(filepath, "r") as f:
                lines = f.readlines()
            with open(filepath, "w") as f:
                for line in lines:
                    if not line.startswith(user_id + ","):
                        f.write(line)

        for file in ["users.txt", "passwords.txt", "grades.txt", "eca.txt"]:
            if os.path.exists(file):
                filter_out(file)

    def generate_report(self):
        subject_totals = [0]*5
        count = 0
        try:
            with open("grades.txt", "r") as f:
                for line in f:
                    grades = list(map(int, line.strip().split(",")[1:]))
                    subject_totals = [x+y for x, y in zip(subject_totals, grades)]
                    count += 1
            averages = [round(t / count, 2) for t in subject_totals]
        except:
            averages = []

        eca_counts = {}
        try:
            with open("eca.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    eca_counts[parts[0]] = len(parts[1:])
        except:
            eca_counts = {}

        most_active = sorted(eca_counts.items(), key=lambda x: x[1], reverse=True)
        return {
            "average_grades": averages,
            "most_active": most_active[:3]
        }


def authenticate(username, password):
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                stored_user, stored_pass = line.strip().split(",")
                if stored_user == username and stored_pass == password:
                    role = User(username).get_role()
                    if role == "admin":
                        return Admin(username)
                    elif role == "student":
                        return User(username)
    except FileNotFoundError:
        return None
    return None


def load_users():
    users = []
    try:
        with open("users.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) >= 4:
                    users.append({
                        "id": data[0],
                        "name": data[1],
                        "email": data[2],
                        "role": data[3]
                    })
    except FileNotFoundError:
        pass
    return users
