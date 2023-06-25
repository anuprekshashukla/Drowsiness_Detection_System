<h1>Drowsiness Detection System(webapp)</h1>
<h2>Motivation:</h2>
According to the National Highway Traffic Safety Administration, every year about 100,000 police-reported crashes involve drowsy driving. These crashes result in more than 1,550 fatalities and 71,000 injuries. The real number may be much higher, however, as it is difficult to determine whether a driver was drowsy at the time of a crash. So, we tried to build a system, that detects whether a person is drowsy and alert him<br>
<h2>Installing and Configuring dlib:</h2>
We need to create an enivronment in order to install dlib, as it cannot be directly installed using pip. So, follow this commands in order to install dlib into your system if you haven't installed it previously. Make sure you have Anaconda installed, as we will be doing everyting in Anaconda Prompt.<br><br>
<h3>Step 1: Update conda</h3>
<div 
  <pre>conda update conda</pre>  
</div>
<h3>Step 2: Update anaconda</h3>
<div 
  <pre>conda update anaconda </pre>  
</div>
<h3>Step 3: Create a virtual environment</h3>
<div 
  <pre>conda create -n env_dlib</pre>  
</div>
<h3>Step 4: Activate the virtual environment</h3>
<div 
  <pre>conda activate env_dlib</pre>  
</div>
<h3>Step 5:  Install dlib</h3>
<div 
  <pre>conda install -c conda-forge dlib</pre>  
</div><br>
If all these steps are completed successfully, then dlib will be installed in the virtual environment env_dlib. Make sure to use this environment to run the entire project.
<h3>Step to deactivate the virtual environment</h3>
<h2>Running the system:</h2>
<h3>Step 1:</h3>
Clone the repository into your system by:<br><br>
git clone https://github.com/anuprekshashukla/Drowsiness_Detection_System.git<br><br>
Or directly download the zip.
<h3>Step 2:</h3>
Download the file shape_predictor_68_face_landmarks.dat . Make sure you download it in the same folder.
<h3>Step 3:</h3>
Install all the system requirments by:<br><br>
pip install -r requirements.txt
<h3>Step 4:</h3>
After the system has been setup. Run the command:<br><br>
python app1.py
<h3>Step 5:</h3>
Open your browser and in the search bar type: localhost:8000 as this port is mostly used by flask. In case, this port is not available in your system, flask will try to use another port. The port number will be displayed in the command prompt. So, type in the same port number in that case as: localhost:<port_number>.<br><br>

After all these steps have been completed successfully, you will see a web page opening up in the browser. Now you are free to explore the system.
<h2>Working Details:</h2>
he basic thing about drowsiness detection is pretty simple. We first detect a face using dlib's frontal face detector. Once the face is detected , we try to detect the facial landmarks in the face using the dlib's landmark predictor. The landmark predictor returns 68 (x, y) coordinates representing different regions of the face, namely - mouth, left eyebrow, right eyebrow, right eye, left eye, nose and jaw. Ofcourse, we don't need all the landmarks, here we need to extract only the eye and the mouth region.<br><br>

Now, after extraxting the landmarks we calculate the<b> Eye Aspect Ratio (EAR)</b> as:
<br>

The eye region is marked by 6 coordinates. These coordinates can be used to find whether the eye is open or closed if the value of EAR is checked with a certain threshold value.

![87878670-62d41400-ca03-11ea-8b96-fc4344c61a21](https://github.com/anuprekshashukla/Drowsiness_Detection_System/assets/83533944/22de8403-76ee-4958-bb84-d80641af2a33)

<p>In the same way I have calculated the aspect ratio for the mouth to detect if a person is yawning. Although, there is no specific metric for calculating this, so I have taken for points, 2 each from the upper and lower lip and calculated the mean distance between them as:</p>
<h2>Result:</h2>
The GUI has been created using basic HTML, CSS and JavaScript and we have used Flask to render the python code into the website. Tkinter has also been used in order to make things simpler. It has 2 buttons: Run and Exit. The GUI
