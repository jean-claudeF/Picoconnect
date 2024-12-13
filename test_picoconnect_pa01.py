from picoconnect_pa01 import create_pico_dictionary, Pico, CMD_TEST

keyword = "SWISS"

create_pico_dictionary()
mypico = Pico(keyword)
mypico.connect()
mypico.execute(CMD_TEST)
mypico.execute("x = 5; print (2* 3.14 * x)")
mypico.list_files()
mypico.read_file("main.py")
mypico.close()

# Here no print function is used, as most functions have printflag = True by default
# Anyway the respose is also returned by the functions
