def read_csv(csv_file):
        """ 
        Read the CSV file using the following format:
        name, email
        
        This csv reader already skips the header
        """
        import csv

        attendee_list = []
        with open(csv_file, mode="r", encoding="UTF-8") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                        attendee_list.append(row)

        return attendee_list
