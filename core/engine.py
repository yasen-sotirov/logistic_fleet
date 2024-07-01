from core.command_factory import CommandFactory

file_path_output = 'output.txt'
open(file_path_output, mode='w').close()
class Engine:
    def __init__(self, factory):
        self._command_factory = factory

    def start(self):
        output: list[str] = []
        while True:
            input_line = input()
            if input_line == '':
                continue
            if input_line.lower() == "end":
                break
            try:
                command = self._command_factory.create(input_line)
                # output.append(command.execute())
                print(command.execute())
                print()
                print()
            except:
                AttributeError
                # output.append(command.execute())
                print(command.execute())
                print()
                print()

        # with open(file_path_output, 'a') as out:
        #     for line in output:
        #         out.write(line + '\n')

        # print("\n".join(output))

 
