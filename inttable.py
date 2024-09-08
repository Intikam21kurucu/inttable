import importlib.util

def load_console_module():
    spec = importlib.util.spec_from_file_location("intconsole_module", "intconsoleV4.py")
    console_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(console_module)
    return console_module

def run_console_function(function_name, *args, **kwargs):
    # İntconsoleV4.py modülünü yükle
    console_module = load_console_module()

    # Fonksiyonun var olup olmadığını kontrol et
    if hasattr(console_module, function_name):
        function_to_run = getattr(console_module, function_name)
        result = function_to_run(*args, **kwargs)
        return result
    else:
        return f"Fonksiyon '{function_name}' bulunamadı."

def execute_command(command):
    # İntconsoleV4.py modülünü yükle
    console_module = load_console_module()

    # help_input değişkenine komut atayıp çalıştır
    console_module.help_input = command
    console_module.execute_help_input()
def use(module):
	execute_command(f"use {module}")
def show_exploits():
	execute_command("show exploits")
def execute_get_input(module):
	run_console_function(get_input, cdn=module)
def login(username, password):
	run_console_function(login, username, password)
def run_exploit():
	execute_command("exploit")
def wifi_scan():
	execute_command("wifi_scan")
def load_plugins(plugin_path):
	execute_command(f"load_plugins {plugin_path}")
def run_plugins(command, *args):
	execute_command("run_plugins {command} {args}")
def list_plugins():
	execute_command("list_plugins")
def check(ip):
	run_console_function(check_ip, ip)