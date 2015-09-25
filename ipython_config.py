
c = get_config()

# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always

# Notebook config
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
#c.NotebookApp.password = 
c.NotebookApp.port = 3000