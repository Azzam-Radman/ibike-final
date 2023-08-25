import pandas as pd
from os import path
import streamlit as st
from streamlit import session_state as ss
import os

def render():
	st.title('Mechanical Engineer')
	
	st.title("Welcome to the Mechanical Engineer Page!")
	# st.image('mechanical_avatar.jpg')

	st.markdown(
		"""
		Your role revolves around selecting the bike **Parts** to manufacture,
		their **Materials**, and the "Manufacturing Processes". You will be given
		each of these in a drop list from which you can make your choices. For each part,
		you will only be shown the most appropriate materials and manufacturing processes.
		""")

	st.markdown("---")

	if not path.isfile(ss.filepath+'parts_selction.csv'):
		selection_df = pd.DataFrame(columns=['Part', 'Material', 'Process'])
	else:
		selection_df = pd.read_csv(ss.filepath+'parts_selction.csv')
		st.markdown("These are the previously selected parts with the materials and the manufacturing processes")
		st.dataframe(selection_df, width=3000)
		st.markdown("---")

	if not path.isfile(ss.filepath+'parts_material_process_justification.csv'):
		justification_df = pd.DataFrame(columns=['Part', 'Material Justification', 'Process Justification'])
	else:
		justification_df = pd.read_csv(ss.filepath+'parts_material_process_justification.csv')
		st.markdown("These are the previously selected parts with justificaions for materials manufacturing processes")
		st.dataframe(justification_df, width=3000)
		st.markdown("---")

	if path.isfile(ss.filepath+'material_feedback.csv'):
		st.markdown("Here is the feedback by the :red[Industrial Engineer] on the selected materials")
		material_feedback_df = pd.read_csv(ss.filepath+'material_feedback.csv')
		st.dataframe(material_feedback_df, width=3000)
		st.markdown("---")

	if path.isfile(ss.filepath+'process_feedback.csv'):
		st.markdown("Here is the feedback by the :red[Industrial Engineer] on the selected manufacturing processes")
		process_feedback_df = pd.read_csv(ss.filepath+'process_feedback.csv')
		st.dataframe(process_feedback_df, width=3000)
		st.markdown("---")

	if path.isfile('pm_feedback_mech_1'):
		st.markdown("""
					Here is the feedback by the :red[Project Manager] on the selected parts, materials, and
					manufacturing processes""")
		with open ('pm_feedback_mech_1', 'rb') as f:
			text = f.read().decode()
		with st.expander("Expand to see feedback!"):
			st.markdown(f":red[{text}]")
		st.markdown("---")

	if path.isfile('pm_feedback_mech_2'):
		st.markdown("""
					Here is the feedback by the :red[Project Manager] on your justificaions""")
		with open ('pm_feedback_mech_2', 'rb') as f:
			text = f.read().decode()
		with st.expander("Expand to see feedback!"):
			st.markdown(f":red[{text}]")
		st.markdown("---")

	parts = ['Select Part',
			'Frame',
			'Handlebars',
			'Stem',
			'Suspension Fork',
			'Disc Brake Rotor',
			'Tire',
			'Rim',
			'Hub',
			'Spoke',
			'Pedal',
			'Crank Arm',
			'Crank Set',
			'Cassette',
			'Chain',
			'Seat Post',
			'Seat',
			]

	col1, col2 = st.columns(2)

	with col1:
		st.markdown('### :blue[Select a part]')
		part = st.selectbox(
			label='Part', 
			options=parts,
			label_visibility='collapsed',
		)


	def make_selections(materials, processes, minimize, maximize):
		with col2:
			st.write('Objectives are:')
			st.write(f'**:red[Minimize:]** {minimize}')
			st.write(f'**:blue[Maximize:]** {maximize}')
		st.markdown("---")

		col3, col4 = st.columns(2)
		with col3:
			st.markdown('#### :blue[Select an appropriate material]')
			st.text("")
			st.text("")
			material = st.selectbox(
				label="Material",
				options=materials,
				label_visibility='collapsed',
			)
			st.text("")
			st.markdown("#### :red[Justify material selection]")
			st.text("")
			st.text("")
			material_just = st.text_area(label="", 
									value="Your justification(100 Chars Max)", 
									label_visibility="collapsed",
									max_chars=100,
									key=0,)
		
		with col4:
			st.markdown('#### :blue[Select an appropriate manufacturing process]')
			process = st.selectbox(
				label="Manufacturing Process",
				options=processes,
				label_visibility='collapsed',
			)
			st.text("")
			st.markdown("#### :red[Justify manufacturing process selection]")
			process_just = st.text_area(label="", 
										value="Your justification (100 Chars Max)", 
										label_visibility="collapsed",
										max_chars=100,
										key=1)
		st.markdown("---")
		return material, process, material_just, process_just


	if part == 'Frame':
		minimize =  'Weight (Density)'
		maximize = 'Ultimate Tensile Strength'
		materials = ['Selec Material',
					'Age-hardening Wrought Al-Alloy',
					'High Carbon Steel',
					'Low Alloy Steel',
					'Titanium Alloys',
					'Wrought Magnesium Alloys'
					]
		processes = ['Selec Manufacturing Process',
					'Forming', 
					'Drawing', 
					'Machining', 
					'Heat Treatment', 
					'Joining',
					'Surface Treatment'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Handlebars':
		minimize =  'Price'
		maximize = 'Young’s Modulus'
		materials = ['Selec Material',
					'Cast Iron - Ductile (Nodular)',
					'Cast Iron - Gray',
					'High Carbon Steel',
					'Low Carbon Steel',
					'Medium Carbon Steel'
					]
		processes = ['Selec Manufacturing Process',
					'Forming', 
					'Drawing', 
					'Machining', 
					'Extrusion', 
					'Heat Treatment',
					'Joining',
					'Surface Treatment'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Stem':
		minimize =  'Price'
		maximize = 'Compressive Strength'
		materials = ['Selec Material',
					'Cast Iron - Ductile (Nodular)',
					'Cast Iron - Gray',
					'High Carbon Steel',
					'Low Alloy Steel',
					'Medium Carbon Steel'
					]
		processes = ['Selec Manufacturing Process',
					'Forming', 
					'Machining',
					'Heat Treatment',
					'Joining',
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Suspension Fork':
		minimize =  'Weight (Density)'
		maximize = 'Compressive Strength'
		materials = ['Selec Material',
					'Boron Carbide',
					'Silica Glass',
					'Silicon',
					'Silicon Carbide',
					'Silicon Nitride'
					]
		processes = ['Selec Manufacturing Process',
					'Extrusion', 
					'Reaction Bonding',
					'Hot Pressing',
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Disc Brake Rotor':
		minimize =  'Price'
		maximize = 'Weight (Density)'
		materials = ['Selec Material',
					'Cast Iron - Ductile (Nodular)',
					'Cast Iron - Gray',
					'High Carbon Steel',
					'Low Alloy Steel',
					'Low Carbon Steel'
					]
		processes = ['Selec Manufacturing Process',
					'Forming', 
					'Drawing', 
					'Machining',
					'Heat Treatment',
					'Joining',
					'Surface Treatment',
					'Casting'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)


	elif part == 'Tire':
		minimize =  'Weight (Density)'
		maximize = 'Moldability'
		materials = ['Selec Material',
					'Butyl Rubber (IIR)',
					'Ethylene Vinyl Acetate (EVA)',
					'Ionomer (I)',
					'Natural Rubber (NR)',
					'Polyethylene'
					]
		processes = ['Selec Manufacturing Process',
					'Polymer Injection Molding', 
					'Polymer Extrusion', 
					'Polymer Thermoforming',
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Rim':
		minimize =  'Weight (Density)'
		maximize = 'Young’s modulus'
		materials = ['Selec Material',
					'Alumina',
					'Aluminium Nitride',
					'Boron Carbide',
					'CFRP - Epoxy Matrix (Isotropic)',
					'Silicon Carbide'
					]
		processes = ['Selec Manufacturing Process',
					'Ring Rolling', 
					'Casting', 
					'Forging',
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Hub':
		minimize =  'Price'
		maximize = 'Fatigue strength at 10^7 cycles'
		materials = ['Selec Material',
					'Cast Iron - Ductile (Nodular)',
					'Cast Iron - Gray',
					'High Carbon Steel',
					]
		processes = ['Selec Manufacturing Process',
					'Rolling', 
					'Cold Forging (Closed die)', 
					'Casting',
					'Drawing',
					'Swaging'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Spoke':
		minimize =  'Price'
		maximize = 'Specific stiffness (level3)'
		materials = ['Selec Material',
					'Cast Iron',
					'Dolomite',
					'Jute Fibre',
					'Kenaf Fibre',
					'Mica (p)'
					]
		processes = ['Selec Manufacturing Process',
					'Casting', 
					'Machining'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Pedal':
		minimize =  'Price'
		maximize = 'Ultimate Tensile Strength'
		materials = ['Selec Material',
					'Cast Iron - Ductile (Nodular)',
					'Cast Iron - Gray',
					'High Carbon Steel',
					'Low Alloy Steel',
					'Medium Carbon Steel'
					]
		processes = ['Selec Manufacturing Process',
					'Forming', 
					'Drawing', 
					'Machining',
					'Heat Treatment',
					'Joining',
					'Surface Treatment'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Crank Arm':
		minimize =  'Weight(Density)'
		maximize = 'Ultimate Tensile Strength'
		materials = ['Selec Material',
					'Bamboo',
					'CFRP - Epoxy Matrix',
					'Low Alloy Steel',
					'Titanium alloys',
					'Wrought Magnesium Alloys'
					]
		processes = ['Selec Manufacturing Process',
					'Casting', 
					'Machining'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Crank Set':
		minimize =  'Weight(Density)'
		maximize = 'Fatigue strength at 10^7 Cycles'
		materials = ['Selec Material',
					'Boron Carbide',
					'CFRP - Epoxy Matrix',
					'Silicon Nitride',
					'Titanium Alloys',
					'Wrought Magnesium Alloys'
					]
		processes = ['Selec Manufacturing Process',
					'Casting', 
					'Machining'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	elif part == 'Cassette':
		minimize =  'Weight(Density)'
		maximize = 'Fatigue strength at 10^7 Cycles'
		materials = ['Selec Material',
					'Butyl Rubber (IIR)',
					'Ethylene Vinyl',
					'Acetate (EVA)',
					'Ionomer(I)',
					'Natural Rubber (NR)',
					'Polyethylene (PE)'
					]
		processes = ['Selec Manufacturing Process',
					'Casting', 
					'Machining'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)


	elif part == 'Chain':
		minimize =  'Price'
		maximize = 'Fatigue strength at 10^7 Cycles'
		materials = ['Selec Material',
					'Medium carbon steel',
					'Low carbon steel',
					'Low alloy steel',
					'Cast iron - gray',
					'Cast iron - ductile (nodular)'
					]
		processes = ['Selec Manufacturing Process',
					'Forming', 
					'Drawing', 
					'Machining',
					'Heat Treatment',
					'Joining',
					'Surface Treatment'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)


	elif part == 'Seat Post':
		minimize =  'Weight (Density)'
		maximize = 'Compressive Strength'
		materials = ['Selec Material',
					'Cast Al-Alloys',
					'Low carbon steel',
					'Stainless Steel Cast',
					'Magnesium Alloys',
					'Low Alloy Steel'
					]
		processes = ['Selec Manufacturing Process',
					'Forming',
					'Heat Treatment',
					'Joining',
					'Surface Treatment'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)


	elif part == 'Seat':
		minimize =  'Weight (Density)'
		maximize = 'Price'
		materials = ['Selec Material',
					'Polyurethane',
					'Rigid Polymer',
					'Foam (HD)',
					'Rigid Polymer Foam (LD)',
					'Flexible Polymer Foam (VLD)',
					'Ceramic Foam'
					]
		processes = ['Selec Manufacturing Process',
					'Injection molding',
					'Open Die Forging',
					'Casting'
					]
		material, process, material_just, process_just = make_selections(materials, processes, minimize, maximize)

	st.text("")
	st.text("")
	st.write(
		"""
		These are your selections. To make a change, go up :point_up:, select the part and 
		continue the process.
		""")

	if st.button('Reset Table', key=-1):
		os.system(ss.filepath+'rm parts_selction.csv')
		os.system(ss.filepath+'rm parts_material_process_justification.csv')

	else:
		try:
			selection_df.loc[len(selection_df)] = [part, material, process]
			selection_df = selection_df.drop_duplicates(subset=['Part'], keep='last')
			selection_df.index = range(1, len(selection_df)+1)
			selection_df.to_csv(ss.filepath+'parts_selction.csv', index=False)
			st.dataframe(selection_df, width=4000)

			justification_df.loc[len(justification_df)] = [part, material_just, process_just]
			justification_df = justification_df.drop_duplicates(subset=['Part'], keep='last')
			justification_df.index = range(1, len(justification_df)+1)
			justification_df.to_csv(ss.filepath+'parts_material_process_justification.csv', index=False)
			st.dataframe(justification_df, width=4000)
		except:
			pass

def feedback():
	# writing
	st.header("Feedback **:red[TO]**")
	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_m_d.txt'):
		with open(ss.filepath+'fb_m_d.txt', 'r') as f:
			text = f.read()

	fb_m_d = st.text_area("Your feedback to the Design Engineer", text)
	if fb_m_d != "" and path.isfile(ss.filepath+'fb_m_d.txt'):
		with open(ss.filepath+"fb_m_d.txt", "w") as f:
			f.write(fb_m_d)
		st.markdown("---")

	if st.button('Clear Feedback', key=10):
		if path.isfile(ss.filepath+'fb_m_d.txt'):
			os.remove(ss.filepath+'fb_m_d.txt')


	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_m_i.txt'):
		with open(ss.filepath+'fb_m_i.txt', 'r') as f:
			text = f.read()

	fb_m_i = st.text_area("Your feedback to the Industrial Engineer", text)
	if fb_m_i != "" and path.isfile(ss.filepath+'fb_m_i.txt'):
		with open(ss.filepath+"fb_m_i.txt", "w") as f:
			f.write(fb_m_i)
		st.markdown("---")

	if st.button('Clear Feedback', key=11):
		if path.isfile(ss.filepath+'fb_m_i.txt'):
			os.remove(ss.filepath+'fb_m_i.txt')

	
	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_m_pm.txt'):
		with open(ss.filepath+'fb_m_pm.txt', 'r') as f:
			text = f.read()

	fb_m_pm = st.text_area("Your feedback to the Project Manager", text)
	if fb_m_pm != "" and path.isfile(ss.filepath+'fb_m_pm.txt'):
		with open(ss.filepath+"fb_m_pm.txt", "w") as f:
			f.write(fb_m_pm)
		st.markdown("---")

	if st.button('Clear Feedback', key=12):
		if path.isfile(ss.filepath+'fb_m_pm.txt'):
			os.remove(ss.filepath+'fb_m_pm.txt')

	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_m_pum.txt'):
		with open(ss.filepath+'fb_m_pum.txt', 'r') as f:
			text = f.read()

	fb_m_pum = st.text_area("Your feedback to the Purchasing Manager", text)
	if fb_m_pum != "" and path.isfile(ss.filepath+'fb_m_pum.txt'):
		with open(ss.filepath+"fb_m_pum.txt", "w") as f:
			f.write(fb_m_pum)
		st.markdown("---")

	if st.button('Clear Feedback', key=13):
		if path.isfile(ss.filepath+'fb_m_pum.txt'):
			os.remove(ss.filepath+'fb_m_pum.txt')


	# reading
	st.header("Feedback **:red[From]**")
	if path.isfile(ss.filepath+'fb_d_m.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Design Engineer]**")
		with open(ss.filepath+'fb_d_m.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")

	if path.isfile(ss.filepath+'fb_i_m.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Industrial Engineer]**")
		with open(ss.filepath+'fb_i_m.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")


	if path.isfile(ss.filepath+'fb_pm_m.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Project Manager]**")
		with open(ss.filepath+'fb_pm_m.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")


	if path.isfile(ss.filepath+'fb_pum_m.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Purchasing Manager]**")
		with open(ss.filepath+'fb_pum_m.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")
