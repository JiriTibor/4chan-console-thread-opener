import requests, json, webbrowser

def get_boards():

    connect = requests.get("https://a.4cdn.org/boards.json")
    boards = connect.json()

    for x in range(1,78):
        print(boards["boards"][x]["board"], ": " , boards["boards"][x]["title"])
    
    return boards

def print_catalog(board):
    board_url = "https://a.4cdn.org/"+board+"/catalog.json"

    connect = requests.get(board_url)
    board_catalog = connect.json()
    for page_number in range(0,len(board_catalog)-1):
        try:
            page = board_catalog[page_number]
        except IndexError:
            pass
        
        for x in range(0,14):
            try:
                print(page["threads"][x]["no"],":", page["threads"][x]["sub"], '\n')
            except KeyError:
                pass

    print("Type the id of thread to open it")
    
    thread_id = input()
    thread_url = "https://boards.4channel.org/"+board+"/thread/"+thread_id
    open_thread(thread_url) 

def open_thread(url):
    webbrowser.register("firefox",
        None,
        webbrowser.BackgroundBrowser("/usr/bin/firefox"))
    
    webbrowser.get("firefox").open(url)

get_boards()
print("choose board: ")
board = input()

print_catalog(board)