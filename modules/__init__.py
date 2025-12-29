def is_running_exe() -> bool:
    return globals().get("__compiled__",False)
