from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import *
from textual.binding import Binding
from pathlib import Path
import os

class FileBrowserApp(App):
    # CSS = """
    # Horizontal {
    #     height: 100%;
    #     background: #1a1b26;
    # }
    
    # DirectoryTree {
    #     width: 100%;
    #     height: 100%;
    #     border: solid #24283b;
    #     background: #1a1b26;
    #     color: #a9b1d6;
    # }
    
    # #search_container {
    #     width: 100%;
    #     height: 100%;
    #     background: #1a1b26;
    # }
    
    # Input {
    #     dock: top;
    #     border: solid #24283b;
    #     background: #1a1b26;
    #     color: #a9b1d6;
    # }
    
    # #results {
    #     background: #1a1b26;
    #     color: #a9b1d6;
    #     height: auto;
    #     padding: 1;
    # }
    
    # TabbedContent {
    #     height: 1fr;
    # }
    # """

    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Leto"):
                yield Markdown("# Leto \n You will be missed")
            with TabPane("Jessica"):
                yield DirectoryTree("./")
            with TabPane("Paul"):
                yield Input(placeholder="First Name")
                yield Static(id="results")

    

    def on_input_changed(self, event: Input.Changed) -> None:
        search_term = event.value.lower()
        results = []
        
        if search_term:
            for root, _, files in os.walk("./"):
                for file in files:
                    if search_term in file.lower():
                        path = Path(root) / file
                        results.append(str(path))
        print(results)
        
        results_widget = self.query_one("#results")
        results_widget.update("\n".join(results) if results else "No matches found")

if __name__ == "__main__":
    app = FileBrowserApp()
    print("Wahoooo")
    app.run()
