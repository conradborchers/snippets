def estimate_reading_time(text, group='Highschool (14-18 years)'):
    """
    Currently only returns lower bound (first entry in tuple)
    Currently returns result in seconds
    """
    # Define reading speeds (words per minute) for different age groups
    reading_speeds = {
        '1st Grade (6-7 years)': (53, 111),
        '2nd Grade (7-8 years)': (89, 149),
        '3rd Grade (8-9 years)': (107, 162),
        '4th Grade (9-10 years)': (123, 180),
        '5th Grade (10-11 years)': (139, 194),
        '6th-8th Grade (11-14 years)': (150, 204),
        'Highschool (14-18 years)': (200, 300),
        'College (18-23 years)': (300, 350),
        'Adults': (220, 350)
    }
    words = len(text.split())
    return words*60/reading_speeds[group][0]

# Example usage
text = "Once upon a time in a land far, far away..."
reading_times = estimate_reading_time(text)
print(text)
print(reading_times, 'seconds')

# References
# Children: Hasbrouck, J., & Tindal, G. (2017). An update to compiled ORF norms (No. 1702). Technical report.
# Adults: Brysbaert, M. (2019). How many words do we read per minute? A review and meta-analysis of reading rate. Journal of memory and language, 109, 104047.
