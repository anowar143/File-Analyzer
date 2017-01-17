class AnalyzeFile:
    def __init__(self, file_input, file_output):
        self.input_file = file_input
        self.output_file = file_output

    def file_reader(self):
        lists = []
        output_file = open(self.output_file + self.input_file, 'w')
        with open(self.input_file) as myFile:
            for num, line in enumerate(myFile, 1):
                if not num == 1:
                    if not line == "":
                        new_data = line.split(" ", 1)[0]
                        lists.append(new_data)
        for item in lists:
            output_file.write("%s\n" % item)
        output_file.close()


data = AnalyzeFile('ra.txt', 'output/')
data.file_reader()
