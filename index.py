from pywebio import start_server
from pywebio.output import *
from pywebio.input import *

def main():
    # Upper bar with dropdown
    put_html("""
    <style>
        body { margin: 0; }
        .navbar {
            width: 100%;
            background: #4a90e2;
            display: flex;
            padding: 10px;
            box-sizing: border-box;
            align-items: center;
        }
        .dropdown {
            position: relative;
            display: inline-block;
        }
        .dropbtn {
            background-color: #4a90e2;
            color: white;
            padding: 8px 16px;
            border: none;
            cursor: pointer;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: white;
            box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
            z-index: 1;
        }
        .dropdown-content a {
            color: black;
            padding: 8px 12px;
            display: block;
            text-decoration: none;
        }
        .dropdown-content a:hover { background-color: #ddd; }
        .dropdown:hover .dropdown-content { display: block; }

        .grid-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 10px;
            padding: 10px;
            height: calc(100vh - 50px);
            box-sizing: border-box;
        }
        .grid-item {
            border: 1px solid #ccc;
            padding: 10px;
            box-sizing: border-box;
        }
    </style>

    <div class="navbar">
        <div class="dropdown">
            <button class="dropbtn">Menu</button>
            <div class="dropdown-content">
                <a href="#">Option 1</a>
                <a href="#">Option 2</a>
                <a href="#">Option 3</a>
            </div>
        </div>
    </div>

    <div class="grid-container">
        <div class="grid-item" id="area1"></div>
        <div class="grid-item" id="area2"></div>
        <div class="grid-item" id="area3"></div>
        <div class="grid-item" id="area4"></div>
    </div>
    """)

    # Main content using pywebio scopes
    with use_scope('area1'):
        put_text("Data Table Placeholder")

    with use_scope('area2'):
        put_text("Histogram Placeholder")

    with use_scope('area3'):
        put_text("Summary Statistics Placeholder")

    with use_scope('area4'):
        put_text("Custom Visualization Placeholder")

start_server(main, port=8080, debug=True)
