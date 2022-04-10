from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style, Button, Frame, Label, Entry, LabelFrame
from tkinter.scrolledtext import ScrolledText
from random import choice


class Window( Tk ):
    def __init__(self):
        Tk.__init__( self )
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.width_window = 488
        self.height_window = 370
        self.geometry(
            f'{self.width_window}x{self.height_window}+{(sw - self.width_window) // 2}+{(sh - self.height_window) // 2}' )
        self.resizable( False, False )
        # self.overrideredirect(True)
        self.title( 'А кто твой Secret Santa?' )
        photo = PhotoImage( file='Санта_Клаус.png' )
        self.iconphoto( False, photo )
        self['bg'] = '#E0E0E0'

        self.set_ui()

    def set_ui(self):
        self.style = Style()
        self.style.theme_use( 'alt' )
        total_data = {'font': ('Arial', 16), 'background': '#E0E0E0'}
        self.style.configure( 'TLabel', **total_data )
        self.style.configure( 'TEntry', **total_data )
        self.style.configure( 'TLabelFrame', **total_data )
        self.style.configure( 'TButton', **total_data )

        self.top_frame = Frame( self ).grid( row=0, column=0 )
        self.lbl_for_num = Label( self.top_frame, text='Введите участников Secret Santa', style='TLabel' )
        btl_del = Button( self.top_frame, text='Очистить', command=self.del_data )
        btl_del.grid( row=0, column=1, padx=5, pady=5, sticky=E )
        label_for_frame_left = Label( text='Отправитель:' )
        self.left_frame = LabelFrame( self.top_frame, labelwidget=label_for_frame_left,
                                      width=self.width_window // 2 - 10,
                                      height=self.height_window - 100 )
        self.text_left = ScrolledText( self.left_frame, width=27, height=16, wrap=WORD )
        label_for_frame_right = Label( text='Получатель:' )
        self.right_frame = LabelFrame( self.top_frame, labelwidget=label_for_frame_right,
                                       width=self.width_window // 2 - 10,
                                       height=self.height_window - 100 )
        self.text_right = ScrolledText( self.right_frame, width=27, height=16, wrap=WORD, state=DISABLED )
        self.btn_exit = Button( self.top_frame, text='Закрыть', command=self.exit_window )
        btn_define = Button( self.top_frame, text='Определить', command=self.set_list_party )
        btn_define.grid( row=2, column=0, padx=5, pady=5, sticky=E )

        self.draw_widgets()

    def draw_widgets(self):
        self.lbl_for_num.grid( row=0, column=0, padx=5, pady=5, sticky=W )
        self.left_frame.grid( row=1, column=0, padx=5, pady=5 )
        self.text_left.grid( row=1, column=0, padx=5, pady=5 )
        self.right_frame.grid( row=1, column=1, padx=5, pady=5 )
        self.text_right.grid( row=1, column=1, padx=5, pady=5 )
        self.btn_exit.grid( row=2, column=1, padx=5, pady=5, sticky=E )


    def run(self):
        self.mainloop()

    def del_data(self):
        self.text_left.delete('1.0', 'end')
        self.text_right.config(state=NORMAL)
        self.text_right.delete('1.0', 'end')
        self.text_right.config(state=DISABLED)

    def exit_window(self):
        choice = messagebox.askyesno( 'Выход из программы', 'Вы действительно хотите закрыть окно?' )
        if choice:
            self.destroy()

    def set_list_party(self):
        self.text_right.config( state=NORMAL )

        first_and_last_name = self.text_left.get( "1.0", "end-1c" ).split( '\n' )
        #print(first_and_last_name)
        selected_pairs = dict.fromkeys( first_and_last_name, 0 )

        for key, value in selected_pairs.items():
            while selected_pairs[key] == 0:
                selected_name = choice( first_and_last_name )
                if key != selected_name and (selected_name not in selected_pairs.values()):
                    selected_pairs[key] = selected_name
                    first_and_last_name.remove( selected_name )
                else:
                    continue
        #print(selected_pairs)
        self.text_right.delete( '1.0', 'end' )
        for key, value in selected_pairs.items():
            #print(value)
            self.text_right.insert( 'end', f'{value}\n' )
        self.text_right.config( state=DISABLED )


if __name__ == '__main__':
    window = Window()
    window.run()


