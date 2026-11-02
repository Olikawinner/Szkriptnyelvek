def clean_comments(input_file, output_file, remove_indented=False):
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    with open(output_file, 'w', encoding='utf-8') as f_out:
        for line in lines:
            if not remove_indented:
                if not line.startswith('#'):
                    f_out.write(line)
            else:
                if not line.strip().startswith('#'):
                    f_out.write(line)

clean_comments('string1.py', 'string1_clean.py', remove_indented=False)

clean_comments('string1.py', 'string1_clean_v2.py', remove_indented=True)