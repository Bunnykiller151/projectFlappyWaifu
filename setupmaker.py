import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Flappy Waifu",
    options={"build_exe": {"packages":["pygame, time, sys, random"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )