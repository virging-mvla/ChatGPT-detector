from driverInputs import driverInputs
from computation import computation
import tkinter as tk

# Create the root window
root = tk.Tk()

# Create the input text box
input_text = tk.Entry(root, width=50)
input_text.pack()



# Create the output text box
output_text = tk.Text(root)
output_text.pack()

# Define the submit function


def submit():
    # Get the input text
    input_str = str(input_text.get())
    print(input_str)

    page1 = driverInputs(input_str)
    page1.loadPage()
    page1.getButtons()

    outForFinal = computation(page1)
    outForFinal.computeFinalVal()

    finalVal = outForFinal.finalVal
    decision = ""
    print(finalVal)
    if finalVal < 50:
    	decision = "Probably Human"
    elif finalVal >= 50:
    	if finalVal < 75:
            decision = "Possibly Human"
    	else:
        	decision = "Definitely AI"
    # Set the output text
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, decision)
# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Start the GUI event loop
root.mainloop()

