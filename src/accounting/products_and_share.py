
application_meta = [
    {
        "name": "easy",
        "id": 1001,
        "share": 0.3
    },
    {
        "name": "app",
        "id": 1002,
        "share": 0.2
    },
    {
        "name": "market",
        "id": 1003,
        "share": 0.2
    },
    {
        "name": "other",
        "id": 1004,
        "share": 0.3
    }
]


def get_app_meta():
    share_sum = 0
    for app in application_meta:
        share_sum += app["share"]
    if share_sum == 1:
        return application_meta
    else:
        print("application share sum is off")
        return False


if __name__ == "__main__":
    check = get_app_meta()
    print("Request Result:\n", check)
    