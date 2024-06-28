a1 = "make money"
a2 = "click on link"
a3 = "join my telegram"
a4 = "win cash prize"
comment= input("Enter your comment: ")
# yaha pe mai comment = input("Enter your comment: ").lower() bhi use kr skte the
#  toh itna baar ni likhna padta if function me 
if (a1 in comment.lower() or a2 in comment.lower() or a3 in comment.lower() or a4 in comment.lower() ) :
    print("Dont spam here ")
else:
    print("Comment sent successfully")
