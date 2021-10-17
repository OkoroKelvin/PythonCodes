# # 6.8 (Challenge: Writing the Word Equivalent of a Check Amount) In check-writing
# # systems, it’s crucial to prevent alteration of check amounts. One common security method
# # requires that the amount be written in numbers and spelled out in words as well. Even if
# # someone can alter the numerical amount of the check, it’s tough to change the amount in
# # words. Create a dictionary that maps numbers to their corresponding word equivalents.
# # Write a script that inputs a numeric check amount that’s less than 1000 and uses the dictionary to write the word equivalent of the amount. For example, the amount 112.43
#
# amount = input("Kindly input your numbers")
# split_amount = amount.split()
# amount_in_words={"1":"ONE","2":"TWO","3":"THREE",
#                  # "4":"FOUR","5"}