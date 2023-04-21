class BuildSubstring:
    def __init__(self, data: dict):
        self.data = data

        self.q = self.build_full_string()

    # def build_date_substring_(self, data: dict)->str:

    #     if self.data['start_date'] != '':

    def build_root_substring(self)->str:
        '''
        Docstring
        '''
    
        if len(self.data['root_terms']) > 0:
            return " & ".join([f'"{f}"' for f in self.data['root_terms']])
        else:
            return ''

    def build_filetype_substring(self)->str:
        '''
        Docstring
        '''
    
        if len(self.data['filetypes']) > 0:
            ft_append = " | ".join([f'filetype:{f}' for f in self.data['filetypes']])
            return f"({ft_append})"
        else:
            return ''


    def build_date_substring(self)->str:
        '''
        Docstring
        '''
        
        start_dt = self.data["start_date"]
        end_dt = self.data["end_date"]
        
        if start_dt != "" and end_dt != "":
            return f'after:{start_dt} & before:{end_dt}'
        elif start_dt == "" and end_dt != "":
            return f'before:{start_dt}'
        elif start_dt != "" and end_dt == "":
            return f'after:{start_dt}'
        elif start_dt == "" and end_dt == "":
            return ""
        else: 
            print("What is this even?")

    # def build_date_substring(self, date: str, isStartDate: bool)->str:
        
    #     if isStartDate:
    #         return f'(after:{date})'
    #     else:
    #         return f'(before:{date})'

    def build_full_string(self)->str:
        '''
        Docstring
        '''

        self.fragments = [
            self.build_root_substring(),
            self.build_date_substring(),
            self.build_filetype_substring()
        ]

        full_str = ' & '.join(self.fragments)


    # def build_full_string_AP(self, data:dict)->str:
    #     full_str = ""

    #     for key in data:

    #         if key == "root_terms":
    #             full_str += " ".join(data[key])
    #         elif key == "start_date":
    #             full_str += self.build_date_substring()
    #         elif key == "end_date":
    #             full_str += self.build_date_substring()
    #         elif key == "filetypes":
    #             full_str += self.build_filetype_substring()
            
    #         full_str += " "
            


        return full_str

def test():
    print("test")
