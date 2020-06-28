import re,os
import log_display


def Searching_errors_in_logs(abs_path):  #function to search the errors in log
    try:
        with open(abs_path, "r") as f:    #opening the log file content
            count = 0
            selected_lines = []
            selected_lines.append("IDENTIFIED ERROR MESSAGES IN THE GIVEN LOG ALONG WITH 2 LINES ABOVE AND BELOW THE ERROR: \n\n")
            logs= f.readlines()     #reading file line by line
            keyword_errors = re.compile(r'FATAL EXCEPTION|SEGMENTATION FAULT|KERNEL PANIC')     #regEx pattern for matching the keywords
            for index, line in enumerate(logs):
                result = keyword_errors.search(line)    #searching for the keywords in file line by line
                if result != None:
                    if count <= 100:
                        count += 1
                        selected_lines.append(('ERROR#{}: \n'.format(count)))
                        selected_lines.append("".join(logs[max(0, index - 2):index]))
                        selected_lines.append("".join(logs[max(0, index):index + 3]))  #collecting the errors and printing on the console
            resultant_errors = filter(lambda i: not re.match(r'^\s*$', i), selected_lines)
            return resultant_errors

    except Exception as e:
        print("File not found")
        print(e.__str__())


def search_str_in_logs(abs_path,entry):
    try:
        with open(abs_path, 'r') as f:
            key_list = []
            list1 = f.readlines()
        #print("list....",list1)
        sub_str = entry.get()
        print(sub_str)
        reg = re.compile(sub_str)
        
        with open("output_file.txt", "w") as fw:
            for i in (list1):
                result = reg.search(i)
                if result != None:
                    fw.write('%s' % i)
                
        return
        
    except Exception as e:
        print("File not found")
        print(e.__str__())