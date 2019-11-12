exit_programme = True
manual_override = False
critical_systems_shutdown = False

if not exit_programme and not critical_systems_shutdown:
    if manual_override:
        print("Shutting down system manually")
    else:
        print("This system will not exit just yet")
elif exit_programme and critical_systems_shutdown is not True:
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")