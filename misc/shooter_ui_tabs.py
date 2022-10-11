from cmath import exp
from tkinter import *
from tkinter import ttk
import uuid


child = Tk()
child.title('Shooter Maintenance')
child.geometry("700x425")
txtfont = "consolas"
label_text_bg="gray"
label_text_fg="black"
txtfont_size="14"
entry_text_fg = "black"
entry_text_bg="white"


notebook = ttk.Notebook(child)
shooter_frame   = Frame(notebook, width=600, height=450)
rifle_frame     = Frame(notebook, width=600, height=450)
scope_frame     = Frame(notebook, width=600, height=450)
cartridge_frame = Frame(notebook, width=600, height=450)

notebook.add(shooter_frame, text = "Shooter Profile")
notebook.add(rifle_frame, text = "Rifle Profile")
notebook.add(scope_frame, text = "Scope Profile")
notebook.add(cartridge_frame, text = "Cartridge Profile")

notebook.pack(expand=True)

   # Shooter
lb_shooter1 = Label(shooter_frame, text="ID",            width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_shooter2 = Label(shooter_frame, text="First Name",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_shooter3 = Label(shooter_frame, text="Last Name",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_shooter4 = Label(shooter_frame, text="ID Number",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_shooter5 = Label(shooter_frame, text="Cell Phone",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_shooter6 = Label(shooter_frame, text="eMail",         width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_shooter7 = Label(shooter_frame, text="Team",          width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_shooter8 = Label(shooter_frame, text="Spotter",       width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

lb_shooter1.grid(row=1, column=0, padx=5, pady=0)
lb_shooter2.grid(row=2, column=0, padx=5, pady=0)
lb_shooter3.grid(row=3, column=0, padx=5, pady=0)
lb_shooter4.grid(row=4, column=0, padx=5, pady=0)
lb_shooter5.grid(row=5, column=0, padx=5, pady=0)
lb_shooter6.grid(row=6, column=0, padx=5, pady=0)
lb_shooter7.grid(row=7, column=0, padx=5, pady=0)
lb_shooter8.grid(row=8, column=0, padx=5, pady=0)

id_value = StringVar()
id_value.set(uuid.uuid4())

# Shooter
crm_shooter_id = Label(shooter_frame, anchor="w", height=1, relief="ridge", textvariable=id_value, font=(txtfont, txtfont_size))
crm_shooter_id.grid(row=1, column=1, padx=20)

crm_shooter_fn = Entry(shooter_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_shooter_fn.grid(row=2, column=1)

crm_shooter_ln = Entry(shooter_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_shooter_ln.grid(row=3, column=1)

crm_shooter_id_number = Entry(shooter_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_shooter_id_number.grid(row=4, column=1)

crm_shooter_cellphone = Entry(shooter_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_shooter_cellphone.grid(row=5, column=1)

crm_shooter_email = Entry(shooter_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_shooter_email.grid(row=6, column=1)

crm_shooter_team = Entry(shooter_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_shooter_team.grid(row=7, column=1)

crm_shooter_spotter = Entry(shooter_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_shooter_spotter.grid(row=8, column=1)




# Rifle
lb_rifle1 = Label(rifle_frame, text="Make",         width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle2 = Label(rifle_frame, text="Model",        width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle3 = Label(rifle_frame, text="Caliber",      width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle4 = Label(rifle_frame, text="Chassis",      width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle5 = Label(rifle_frame, text="Trigger",      width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle6 = Label(rifle_frame, text="Break",        width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle7 = Label(rifle_frame, text="Supressor",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle8 = Label(rifle_frame, text="Weight (lb)",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle9 = Label(rifle_frame, text="Bipod",        width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_rifle10 = Label(rifle_frame, text="Software",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

lb_rifle1.grid(row=1, column=0, padx=5, pady=0)
lb_rifle2.grid(row=2, column=0, padx=5, pady=0)
lb_rifle3.grid(row=3, column=0, padx=5, pady=0)
lb_rifle4.grid(row=4, column=0, padx=5, pady=0)
lb_rifle5.grid(row=5, column=0, padx=5, pady=0)
lb_rifle6.grid(row=6, column=0, padx=5, pady=0)
lb_rifle7.grid(row=7, column=0, padx=5, pady=0)
lb_rifle8.grid(row=8, column=0, padx=5, pady=0)
lb_rifle9.grid(row=9, column=0, padx=5, pady=0)
lb_rifle10.grid(row=10, column=0, padx=5, pady=0)

crm_rifle_make = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_make.grid(row=1, column=1)

crm_rifle_model = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_model.grid(row=2, column=1)

crm_rifle_cal = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_cal.grid(row=3, column=1)

crm_rifle_chassis = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_chassis.grid(row=4, column=1)

crm_rifle_trigger = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_trigger.grid(row=5, column=1)

crm_rifle_break = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_break.grid(row=6, column=1)

crm_rifle_supressor = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_supressor.grid(row=7, column=1)

crm_rifle_weight = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_weight.grid(row=8, column=1)

crm_rifle_bipod = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_bipod.grid(row=9, column=1)

crm_rifle_software = Entry(rifle_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_rifle_software.grid(row=10, column=1)



# Scope
lb_scope1 = Label(scope_frame, text="Make",     width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope2 = Label(scope_frame, text="Model",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope3 = Label(scope_frame, text="Rings",    width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope4 = Label(scope_frame, text="MOA Rise", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

lb_scope1.grid(row=1, column=0, padx=5, pady=0)
lb_scope2.grid(row=2, column=0, padx=5, pady=0)
lb_scope3.grid(row=3, column=0, padx=5, pady=0)
lb_scope4.grid(row=4, column=0, padx=5, pady=0)

crm_scope_make = Entry(scope_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_scope_make.grid(row=1, column=1, padx=5, pady=0)

crm_scope_model = Entry(scope_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_scope_model.grid(row=2, column=1, padx=5, pady=0)

crm_scope_rings = Entry(scope_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_scope_rings.grid(row=3, column=1, padx=5, pady=0)

crm_scope_moa_rise = Entry(scope_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_scope_moa_rise.grid(row=4, column=1, padx=5, pady=0)


# Cartridge
lb_scope1 = Label(cartridge_frame, text="Brass",        width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope2 = Label(cartridge_frame, text="Bullet Make",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope3 = Label(cartridge_frame, text="Bullet Model", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope4 = Label(cartridge_frame, text="Bullet Weight",width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope5 = Label(cartridge_frame, text="Primer Make",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope6 = Label(cartridge_frame, text="Primer Model", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope7 = Label(cartridge_frame, text="Powder Make",  width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))
lb_scope8 = Label(cartridge_frame, text="Powder Model", width=25, height=2, anchor="w", bg=label_text_bg, fg=label_text_fg, font=(txtfont, txtfont_size))

lb_scope1.grid(row=1, column=0, padx=5, pady=0)
lb_scope2.grid(row=2, column=0, padx=5, pady=0)
lb_scope3.grid(row=3, column=0, padx=5, pady=0)
lb_scope4.grid(row=4, column=0, padx=5, pady=0)
lb_scope5.grid(row=5, column=0, padx=5, pady=0)
lb_scope6.grid(row=6, column=0, padx=5, pady=0)
lb_scope7.grid(row=7, column=0, padx=5, pady=0)
lb_scope8.grid(row=8, column=0, padx=5, pady=0)

crm_cartridge_brass_make = Entry(cartridge_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_cartridge_brass_make.grid(row=1, column=1, padx=5, pady=0)

crm_cartridge_bullet_make = Entry(cartridge_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_cartridge_bullet_make.grid(row=2, column=1, padx=5, pady=0)

crm_cartridge_bullet_model = Entry(cartridge_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_cartridge_bullet_model.grid(row=3, column=1, padx=5, pady=0)

crm_cartridge_bullet_weight = Entry(cartridge_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_cartridge_bullet_weight.grid(row=4, column=1, padx=5, pady=0)

crm_cartridge_primer_make = Entry(cartridge_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_cartridge_primer_make.grid(row=5, column=1, padx=5, pady=0)

crm_cartridge_primer_model = Entry(cartridge_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_cartridge_primer_model.grid(row=6, column=1, padx=5, pady=0)

crm_cartridge_powder_make = Entry(cartridge_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_cartridge_powder_make.grid(row=7, column=1, padx=5, pady=0)

crm_cartridge_powder_model = Entry(cartridge_frame, width=30, fg=entry_text_fg, bg=entry_text_bg, font=(txtfont, txtfont_size))
crm_cartridge_powder_model.grid(row=8, column=1, padx=5, pady=0)

child.mainloop()