from blog import Blog

MENU_PROMT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to create one, or 'q' to quit!"
blogs = {} # blog name : blog object

def menu():
    selection = input(MENU_PROMT)
    while selection != "q":
        if selection == "c":
            ask_to_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_to_read_blog()
        elif selection == "p":
            ask_to_create_post()
        selection = input(MENU_PROMT)

def ask_to_create_blog():
    title = input("Enter your blog title: ")
    author = input("Enter your name: ")

    blogs[title] = Blog(title, author)

def ask_to_read_blog():
    pass

def ask_to_create_post():
    pass

def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")