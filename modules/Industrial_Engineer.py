import streamlit as st
from streamlit import session_state as ss
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from os import path
import seaborn as sns

def render():
	st.title('Industrial Engineer')
	
	st.write("Welcome to the Industrial Engineer Page!")
	
	def forecasting(seed):
	    st.markdown("---")
	    np.random.seed(seed)
	    with st.expander('See last N-month demand and invetory'):
	        size = st.slider("Period of Visualization (Months)", 1, 12, 12)
	        readings = np.random.randint(50, 400, size=(size,))
	        in_stock = np.random.randint(50, 400, size=(size,))
	        mean = np.mean(np.float32(readings))
	        suggested_order = mean - np.float32(in_stock[-1])
	        time = list(range(1-size, 1))
	        fig, ax = plt.subplots()
	        fig.figsize = (12, 6)
	
	        data1 = pd.DataFrame({'Month':time,
	                            'Reading': in_stock, # inventory
	                            })
	        data2 = pd.DataFrame({'Month':time,
	                            'Reading': readings, # demand
	                            })
	
	        data = pd.concat([data1, data2], axis=0)
	        data['Type'] = ['Inventory']*(len(data)//2) + ['Demand']*(len(data)//2)
	
	        sns.barplot(data=data, x='Month', y='Reading', hue='Type', ax=ax, alpha=0.7)
	        ax.axhline(y=mean, c='red', linestyle='--')
	        st.pyplot(fig)
	        st.markdown("---")
	    return suggested_order
	
	st.markdown(
		"""
		Your role revolves around two main points. You will forecast the demand and then order the appropriate quantities based on the forecasting results. You will be given a drop list for all the bike parts.  
	""")
	
	st.text("")

	st.title(':blue[Demand Forecasting]')

	st.markdown("""
	To forecast the demand,  you will  be provided with the quatities of each part per bike and
	shown the demand for the last 12 months for each part you expand. It will show a line graph 
	encompassing the demand, the inventory level, and the moving average demand for the last 12 months. 
	We also provide you with an initial value that you can use for your prediction. The initial value is
	average demand minus the current invetory. 
	""")
	
	st.markdown("---")
	st.markdown('#### :blue[Select Bike Parts to Order]')
	st.markdown("""
				You can do this sequentially. Each time you can select one part, then define the
				order quatity.
				""")

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
	
	np.random.seed(123)
	lead_times = np.random.randint(7, 120, size=len(parts))
	
	col1, col2 = st.columns(2)

	with col1:
		part = st.selectbox(
							label='Part', 
							options=parts,
							label_visibility='collapsed',
							key=5,
							)
	
	if part != "Select Part":
		np.random.seed(123)
		seeds = np.random.randint(1, 1000, size=(len(parts),))
		idx = parts.index(part)

		with col2:
			st.markdown(f":blue[Lead time is (Days):] :red[{lead_times[idx]}]")
		seed = seeds[idx]

		st.text('')

		suggested_order = forecasting(seed)
		if suggested_order > 0:
			qty = int(suggested_order)
		else:
			qty = 0

		st.text('')
		st.markdown('#### :blue[Choose the order quantity]')
		st.markdown('The initial value given below is calculated as follows:')
		st.latex('Order = Mean~Demand - Current~Invetory')
		order_qty = st.number_input('Quantity (The initial value is = mean demand - invetory)', 
									label_visibility='collapsed',
									value=qty, min_value=0)
		st.markdown("---")

		if not path.isfile(ss.filepath+'orders.csv'):
			orders_df = pd.DataFrame(columns=['Part', 'Qty'])

		else:
			orders_df = pd.read_csv(ss.filepath+'orders.csv')

		if st.button('Reset Table', key=8):
			os.system(ss.filepath+'rm orders.csv')
		else:
			try:
				orders_df.loc[len(orders_df)] = [part, order_qty]
				orders_df = orders_df.drop_duplicates(subset=['Part'], keep='last')
				orders_df.index = range(1, len(orders_df)+1)
				orders_df.to_csv(ss.filepath+'orders.csv', index=False)
				st.text('')
				st.text('')
				st.text('')
				st.write('### Your ordered parts and quantities')
				orders_df.index = list(range(1, len(orders_df)+1))
				orders_df.to_csv(ss.filepath+'orders.csv', index=False)
			except:
				pass

	try:
		st.dataframe(orders_df, width=3000)
	except:
		pass
	
	
def feedback():
	# writing
	st.header("Feedback **:red[TO]**")
	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_i_d.txt'):
		with open(ss.filepath+'fb_i_d.txt', 'r') as f:
			text = f.read()

	fb_i_d = st.text_area("Your feedback to the Design Engineer", text)
	if fb_i_d != "" and path.isfile(ss.filepath+'fb_i_d.txt'):
		with open(ss.filepath+"fb_i_d.txt", "w") as f:
			f.write(fb_i_d)
		st.markdown("---")

	if st.button('Clear Feedback', key=0):
		if path.isfile(ss.filepath+'fb_i_d.txt'):
			os.remove(ss.filepath+'fb_i_d.txt')


	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_i_m.txt'):
		with open(ss.filepath+'fb_i_m.txt', 'r') as f:
			text = f.read()

	fb_i_m = st.text_area("Your feedback to the Mechanical Engineer", text)
	if fb_i_m != "" and path.isfile(ss.filepath+'fb_i_m.txt'):
		with open(ss.filepath+"fb_i_m.txt", "w") as f:
			f.write(fb_i_m)
		st.markdown("---")

	if st.button('Clear Feedback', key=1):
		if path.isfile(ss.filepath+'fb_i_m.txt'):
			os.remove(ss.filepath+'fb_i_m.txt')

	
	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_i_pm.txt'):
		with open(ss.filepath+'fb_i_pm.txt', 'r') as f:
			text = f.read()

	fb_i_pm = st.text_area("Your feedback to the Project Manager", text)
	if fb_i_pm != "" and path.isfile(ss.filepath+'fb_i_pm.txt'):
		with open(ss.filepath+"fb_i_pm.txt", "w") as f:
			f.write(fb_i_pm)
		st.markdown("---")

	if st.button('Clear Feedback', key=2):
		if path.isfile(ss.filepath+'fb_i_pm.txt'):
			os.remove(ss.filepath+'fb_i_pm.txt')


	st.markdown("---")
	text = ""
	if path.isfile(ss.filepath+'fb_i_pum.txt'):
		with open(ss.filepath+'fb_i_pum.txt', 'r') as f:
			text = f.read()

	fb_i_pum = st.text_area("Your feedback to the Purchasing Manager", text)
	if fb_i_pum != "" and path.isfile(ss.filepath+'fb_i_pum.txt'):
		with open(ss.filepath+"fb_i_pum.txt", "w") as f:
			f.write(fb_i_pum)
		st.markdown("---")

	if st.button('Clear Feedback', key=3):
		if path.isfile(ss.filepath+'fb_i_pum.txt'):
			os.remove(ss.filepath+'fb_i_pum.txt')


	# reading
	st.header("Feedback **:red[From]**")
	if path.isfile(ss.filepath+'fb_d_i.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Design Engineer]**")
		with open(ss.filepath+'fb_d_i.txt', 'r') as f:
			text = f.read()
		st.write(text)
		st.markdown("---")

	if path.isfile(ss.filepath+'fb_m_i.txt'):
		st.markdown("---")
		st.write("Feedback from the **:red[Mechanical Engineer]**")
		with open(ss.filepath+'fb_m_i.txt', 'r') as f:
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
