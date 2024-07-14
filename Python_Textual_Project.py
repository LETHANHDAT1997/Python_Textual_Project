from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, SelectionList
from textual.widgets.selection_list import Selection
from textual.containers import Horizontal


class Window_CheckList_Function(App[None]):
    CSS_PATH = "selection_list.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(): 
            yield SelectionList[int](  
                Selection("Falken's Maze", 0, True),
                Selection("Black Jack", 1),
                Selection("Gin Rummy", 2),
                Selection("Hearts", 3),
                Selection("Bridge", 4),
                Selection("Checkers", 5),
                Selection("Chess", 6, True),
                Selection("Poker", 7),
                Selection("Fighter Combat", 8, True),
                Selection("Falken's Maze", 0, True),
                Selection("Black Jack", 1),
                Selection("Gin Rummy", 2),
                Selection("Hearts", 3),
                Selection("Bridge", 4),
                Selection("Checkers", 5),
                Selection("Chess", 6, True),
                Selection("Poker", 7),
                Selection("Fighter Combat", 8, True),
                Selection("Falken's Maze", 0, True),
                Selection("Black Jack", 1),
                Selection("Gin Rummy", 2),
                Selection("Hearts", 3),
                Selection("Bridge", 4),
                Selection("Checkers", 5),
                Selection("Chess", 6, True),
                Selection("Poker", 7),
                Selection("Fighter Combat", 8, True),
                Selection("Falken's Maze", 0, True),
                Selection("Black Jack", 1),
                Selection("Gin Rummy", 2),
                Selection("Hearts", 3),
                Selection("Bridge", 4),
                Selection("Checkers", 5),
                Selection("Chess", 6, True),
                Selection("Poker", 7),
                Selection("Fighter Combat", 8, True),
                id="SelectionListEnable",
                name= "ENABLES"
            ) 
            
            yield SelectionList[int](  
                Selection("Falken's Maze", 0, True),
                Selection("Black Jack", 1),
                Selection("Gin Rummy", 2),
                Selection("Hearts", 3),
                Selection("Bridge", 4),
                Selection("Checkers", 5),
                Selection("Chess", 6, True),
                Selection("Poker", 7),
                Selection("Fighter Combat", 8, True),
                Selection("Falken's Maze", 0, True),
                Selection("Black Jack", 1),
                Selection("Gin Rummy", 2),
                Selection("Hearts", 3),
                Selection("Bridge", 4),
                Selection("Checkers", 5),
                Selection("Chess", 6, True),
                Selection("Poker", 7),
                Selection("Fighter Combat", 8, True),
                Selection("Falken's Maze", 0, True),
                Selection("Black Jack", 1),
                Selection("Gin Rummy", 2),
                Selection("Hearts", 3),
                Selection("Bridge", 4),
                Selection("Checkers", 5),
                Selection("Chess", 6, True),
                Selection("Poker", 7),
                Selection("Fighter Combat", 8, True),
                Selection("Falken's Maze", 0, True),
                Selection("Black Jack", 1),
                Selection("Gin Rummy", 2),
                Selection("Hearts", 3),
                Selection("Bridge", 4),
                Selection("Checkers", 5),
                Selection("Chess", 6, True),
                Selection("Poker", 7),
                Selection("Fighter Combat", 8, True),
                id="SelectionListDisable",
                name= "DISABLES"
            )

        yield Footer()
    
    def on_mount(self) -> None:
        self.get_widget_by_id("SelectionListEnable").border_title = 'ENABLES'
        self.get_widget_by_id("SelectionListDisable").border_title = 'DISABLES'
        # print(self.get_widget_by_id("SelectionListDisable").get_option_at_index(-1))
        self.get_widget_by_id("SelectionListDisable").add_option(("5sdfsdfsdfds", 5))
        self.get_widget_by_id("SelectionListDisable").select(Selection("5sdfsdfsdfds", 5))
if __name__ == "__main__":
    Window_CheckList_Function().run()