import subprocess

if __name__ == "__main__":
    # test name
    print('Testing name functionality...')

    # test with capital letter
    output = subprocess.Popen(['py', '../code/tool.py', '-name', 'GREEN', 'data.csv'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    lines_str = str(output.communicate()[0], encoding = 'utf-8')
    lines = lines_str.split('\r\n')
    # Need to abandon the header and an end resulted from spliting
    # Same operation will be done in the following test results
    if len(lines) - 2 == 1:
        print('Name Test 1 pass.')
    else:
        print('Name Test 1 fail.')

    # test with regular expression 
    output = subprocess.Popen(['py', '../code/tool.py', '-name', 'j+', 'data.csv'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    lines_str = str(output.communicate()[0], encoding = 'utf-8')
    lines = lines_str.split('\r\n')
    if len(lines) - 2 == 3:
        print('Name Test 2 pass.')
    else:
        print('Name Test 2 fail.')

    # test email
    print('Testing email functionality...')

    # test with capital leter 
    output = subprocess.Popen(['py', '../code/tool.py', '-email', '@GMAIL', 'data.csv'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    lines_str = str(output.communicate()[0], encoding = 'utf-8')
    lines = lines_str.split('\r\n')
    if len(lines) - 2 == 5:
        print('Email Test 1 pass.')
    else:
        print('Email Test 1 fail.')

    # test with regular expression 
    output = subprocess.Popen(['py', '../code/tool.py', '-email', 'gre.n', 'data.csv'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    lines_str = str(output.communicate()[0], encoding = 'utf-8')
    lines = lines_str.split('\r\n')
    if len(lines) - 2 == 1:
        print('Email Test 2 pass.')
    else:
        print('Email Test 2 fail.')

    # test gpa
    print('Testing gpa functionality...')

    #test specific gpa
    output = subprocess.Popen(['py', '../code/tool.py', '-gpa', '4.0', 'data.csv'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    lines_str = str(output.communicate()[0], encoding = 'utf-8')
    lines = lines_str.split('\r\n')
    expected = ['Marsha', 'Tiffany']
    success = True
    for line in lines[1:len(lines)-1]:
        line = line.split('\t')
        if line[0] not in expected:
            success = False
    if success:
        print('GPA Test 1 pass.')
    else:
        print('GPA Test 1 fail.')

    #test below the level
    output = subprocess.Popen(['py', '../code/tool.py', '-gpa', '4.0-', 'data.csv'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    lines_str = str(output.communicate()[0], encoding = 'utf-8')
    lines = lines_str.split('\r\n')
    if len(lines) - 2 == 10:
        print('GPA Test 2 pass.')
    else:
        print('GPA Test 2 fail.')
    
    #test above the level
    output = subprocess.Popen(['py', '../code/tool.py', '-gpa', '3.0+', 'data.csv'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    lines_str = str(output.communicate()[0], encoding = 'utf-8')
    lines = lines_str.split('\r\n')
    if len(lines) - 2 == 8:
        print('GPA Test 3 pass.')
    else:
        print('GPA Test 3 fail.')

