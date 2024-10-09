from harlequin.keymap import HarlequinKeyBinding, HarlequinKeyMap

VSCODE_APP_BINDINGS = [
    HarlequinKeyBinding("ctrl+q", "quit"),
    HarlequinKeyBinding("f1", "help"),
    HarlequinKeyBinding("f2", "focus_query_editor"),
    HarlequinKeyBinding("f5", "focus_results_viewer"),
    HarlequinKeyBinding("f6", "focus_data_catalog"),
    HarlequinKeyBinding("f8", "show_query_history"),
    HarlequinKeyBinding("ctrl+b,f9", "toggle_sidebar"),
    HarlequinKeyBinding("f10", "toggle_full_screen"),
    HarlequinKeyBinding("ctrl+e", "show_data_exporter"),
    HarlequinKeyBinding("ctrl+r", "refresh_catalog"),
    HarlequinKeyBinding("tab", "focus_next"),
    HarlequinKeyBinding("shift+tab", "focus_previous"),
]
VSCODE_EDITOR_BINDINGS = [
    HarlequinKeyBinding("ctrl+n", "code_editor.new_buffer"),
    HarlequinKeyBinding("ctrl+w", "code_editor.close_buffer"),
    HarlequinKeyBinding("ctrl+k", "code_editor.next_buffer"),
    HarlequinKeyBinding(
        "ctrl+enter,ctrl+j",
        "code_editor.run_query",
        key_display="^⏎ or ^j",
    ),
    HarlequinKeyBinding("f4", "code_editor.format_buffer"),
    HarlequinKeyBinding("ctrl+s", "code_editor.save_buffer"),
    HarlequinKeyBinding("ctrl+o", "code_editor.load_buffer"),
    HarlequinKeyBinding("ctrl+f", "code_editor.find"),
    HarlequinKeyBinding("f3", "code_editor.find_next"),
    HarlequinKeyBinding("ctrl+g", "code_editor.goto_line"),
    HarlequinKeyBinding("up", "code_editor.cursor_up"),
    HarlequinKeyBinding("down", "code_editor.cursor_down"),
    HarlequinKeyBinding("left", "code_editor.cursor_left"),
    HarlequinKeyBinding("right", "code_editor.cursor_right"),
    HarlequinKeyBinding("ctrl+left", "code_editor.cursor_word_left"),
    HarlequinKeyBinding("ctrl+right", "code_editor.cursor_word_right"),
    HarlequinKeyBinding("home", "code_editor.cursor_line_start"),
    HarlequinKeyBinding("end", "code_editor.cursor_line_end"),
    HarlequinKeyBinding("ctrl+home", "code_editor.cursor_doc_start"),
    HarlequinKeyBinding("ctrl+end", "code_editor.cursor_doc_end"),
    HarlequinKeyBinding("pageup", "code_editor.cursor_page_up"),
    HarlequinKeyBinding("pagedown", "code_editor.cursor_page_down"),
    HarlequinKeyBinding("shift+up", "code_editor.select_up"),
    HarlequinKeyBinding("shift+down", "code_editor.select_down"),
    HarlequinKeyBinding("shift+left", "code_editor.select_left"),
    HarlequinKeyBinding("shift+right", "code_editor.select_right"),
    HarlequinKeyBinding("ctrl+shift+left", "code_editor.select_word_left"),
    HarlequinKeyBinding("ctrl+shift+right", "code_editor.select_word_right"),
    HarlequinKeyBinding("shift+home", "code_editor.select_line_start"),
    HarlequinKeyBinding("shift+end", "code_editor.select_line_end"),
    HarlequinKeyBinding("ctrl+shift+home", "code_editor.select_doc_start"),
    HarlequinKeyBinding("ctrl+shift+end", "code_editor.select_doc_end"),
    HarlequinKeyBinding("ctrl+a", "code_editor.select_all"),
    HarlequinKeyBinding("ctrl+up", "code_editor.scroll_up_one"),
    HarlequinKeyBinding("ctrl+down", "code_editor.scroll_down_one"),
    HarlequinKeyBinding("ctrl+underscore", "code_editor.toggle_comment"),
    HarlequinKeyBinding("ctrl+x", "code_editor.cut"),
    HarlequinKeyBinding("ctrl+c", "code_editor.copy"),
    HarlequinKeyBinding("ctrl+u,ctrl+v,shift+insert", "code_editor.paste"),
    HarlequinKeyBinding("ctrl+z", "code_editor.undo"),
    HarlequinKeyBinding("ctrl+y", "code_editor.redo"),
    HarlequinKeyBinding("backspace", "code_editor.delete_left"),
    HarlequinKeyBinding("delete", "code_editor.delete_right"),
    HarlequinKeyBinding("shift+delete", "code_editor.delete_line"),
]
VSCODE_DATA_CATALOG_BINDINGS = [
    HarlequinKeyBinding("j", "data_catalog.previous_tab"),
    HarlequinKeyBinding("k", "data_catalog.next_tab"),
    HarlequinKeyBinding(
        "ctrl+enter,ctrl+j",
        "data_catalog.insert_name",
        key_display="^⏎ or ^j",
    ),
    HarlequinKeyBinding("ctrl+c", "data_catalog.copy_name"),
    HarlequinKeyBinding("enter", "data_catalog.select_cursor"),
    HarlequinKeyBinding("space", "data_catalog.toggle_node"),
    HarlequinKeyBinding("up", "data_catalog.cursor_up"),
    HarlequinKeyBinding("down", "data_catalog.cursor_down"),
    HarlequinKeyBinding("full_stop", "data_catalog.show_context_menu"),
    HarlequinKeyBinding("escape", "data_catalog.hide_context_menu"),
]
VSCODE_RESULTS_VIEWER_BINDINGS = [
    HarlequinKeyBinding("j", "results_viewer.previous_tab"),
    HarlequinKeyBinding("k", "results_viewer.next_tab"),
    HarlequinKeyBinding("ctrl+c", "results_viewer.copy_selection"),
    HarlequinKeyBinding("enter", "results_viewer.select_cursor"),
    HarlequinKeyBinding("up", "results_viewer.cursor_up"),
    HarlequinKeyBinding("down", "results_viewer.cursor_down"),
    HarlequinKeyBinding("left", "results_viewer.cursor_left"),
    HarlequinKeyBinding("right", "results_viewer.cursor_right"),
    HarlequinKeyBinding("ctrl+left", "results_viewer.cursor_row_start"),
    HarlequinKeyBinding("ctrl+right", "results_viewer.cursor_row_end"),
    HarlequinKeyBinding("ctrl+up,home", "results_viewer.cursor_column_start"),
    HarlequinKeyBinding("ctrl+down,end", "results_viewer.cursor_column_end"),
    HarlequinKeyBinding("tab", "results_viewer.cursor_next_cell"),
    HarlequinKeyBinding("shift+tab", "results_viewer.cursor_previous_cell"),
    HarlequinKeyBinding("pageup", "results_viewer.cursor_page_up"),
    HarlequinKeyBinding("pagedown", "results_viewer.cursor_page_down"),
    HarlequinKeyBinding("ctrl+home", "results_viewer.cursor_table_start"),
    HarlequinKeyBinding("ctrl+end", "results_viewer.cursor_table_end"),
    HarlequinKeyBinding("shift+up", "results_viewer.select_up"),
    HarlequinKeyBinding("shift+down", "results_viewer.select_down"),
    HarlequinKeyBinding("shift+left", "results_viewer.select_left"),
    HarlequinKeyBinding("shift+right", "results_viewer.select_right"),
    HarlequinKeyBinding("ctrl+shift+left", "results_viewer.select_row_start"),
    HarlequinKeyBinding("ctrl+shift+right", "results_viewer.select_row_end"),
    HarlequinKeyBinding(
        "ctrl+shift+up,shift+home", "results_viewer.select_column_start"
    ),
    HarlequinKeyBinding(
        "ctrl+shift+down,shift+end", "results_viewer.select_column_end"
    ),
    HarlequinKeyBinding("shift+pageup", "results_viewer.select_page_up"),
    HarlequinKeyBinding("shift+pagedown", "results_viewer.select_page_down"),
    HarlequinKeyBinding("ctrl+shift+home", "results_viewer.select_table_start"),
    HarlequinKeyBinding("ctrl+shift+end", "results_viewer.select_table_end"),
    HarlequinKeyBinding("ctrl+a", "results_viewer.select_all"),
]

VSCODE_HISTORY_SCREEN_BINDINGS = [
    HarlequinKeyBinding("enter", "history_screen.select_query"),
    HarlequinKeyBinding("escape", "history_screen.cancel"),
]


VSCODE = HarlequinKeyMap(
    name="vscode",
    bindings=[
        *VSCODE_APP_BINDINGS,
        *VSCODE_EDITOR_BINDINGS,
        *VSCODE_DATA_CATALOG_BINDINGS,
        *VSCODE_RESULTS_VIEWER_BINDINGS,
        *VSCODE_HISTORY_SCREEN_BINDINGS,
    ],
)
