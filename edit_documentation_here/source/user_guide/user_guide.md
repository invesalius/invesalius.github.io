# User Manual

## Introduction

This manual aims to guide the end users in the application of InVesalius
tools. The manual also presents some concepts to facilitate the use of the
software.


### Important Concepts

Detailed in this section is a list of concepts essential to better
understand and operate the software.

#### DICOM (*Digital Image Communications in Medicine*)

DICOM is a standard the transmission, storage and treatment of medical
images. The standard encompasses various origins of medical images, such
as images emanating from computed tomography (CT) equipment, magnetic
resonance, ultrasound, and electrocardiogram, among others.

A DICOM image consists of two main components, namely, an array
containing the pixels of the image and a set of meta-information. This
information includes, but is not limited to, patient name, mode image
and the image position in relation to the space (in the case of CT and
MRI).

#### Computed Tomography — Medical

Computed tomography indicates the radiodensity of tissues, i.e., the
average X-ray absorption by the tissues. The radiodensity reading is
translated into an image gray levels, called the Hounsfield scale, named
Godfrey Newbold Hounsfield, one of the creators of the first CT scan.

```{figure} images/tomografo.jpg
:name: ct_scanner
:align: center

Meidcal CT scanner - www.toshibamedical.com.br
```

Most modern CT scanning appliances are equipped with a radiation emitter
and a sensor bank (with channels ranging from 2 to 256), which circle
the patient while the stretcher is moved, forming a spiral. This
generates a large number of images simultaneously, with little emission
of X-rays.

##### Hounsfield Scale

As mentioned in the previous section, the CT images are generated in
gray levels, expressed in Hounsfield (HU), wherein lighter shades
represent denser matter, and the darker, less dense matter such as skin
and brain tissue.

The table below presents some materials and their
respective values in Hounsfield Units (HU).

| Material | HU            |
|----------|---------------|
| Air      | -1000 or less |
| Fat      | -120          |
| Water    | 0             |
| Muscle   | 40            |
| Contrast | 130           |
| Bone     | 400 or more   |


#### Computed Tomography - Dental (CBCT)

Dental CT commonly works with less radiation emission compared to
medical CT, and therefore makes it possible to view more details of
delicate regions such as alveolar cortical.

```{figure} images/feixe_conico.jpg
:name: dental_tomography
:align: left

Dental tomography -
www.kavo.com.br
```

Image acquisition is performed with the patient positioned vertically
(as opposed to medical tomography in which the patient is horizontal). A
transmitter X-ray surrounds the patient's skull, forming an arc of
180° or 360°. The images generated are compiled as a
volume of the patient's skull. This volume is then \"sliced\" by the
software into individual layers, being able to generate images with
different spacing or fields of view, such as a panoramic view of the
region of interest.

The images acquired by dental scanners often require more post-processing
when it is necessary to separate (segmental) certain
structures using other software such as InVesalius. This is because,
typically, these images have more gray levels than, which makes use of
segmentation patterns (preset) less. Another very common feature in the
images of provincial dental CT scanners is the high presence of speckle
noise and other forms of noise typically caused by the presence of
amalgam prosthetics.

#### Magnetic Resonance Imaging - MRI

MRI is an examination performed without the use of ionizing radiation.
Instead, it uses a strong magnetic field to align the atoms of any
element present in our body, most commonly hydrogen. After alignment,
radio waves are triggered to excite atoms. The sensors measure the time
that the hydrogen atoms take to realign. This makes it possible to
distinguish between different tissues, as different types possess
different quantities of hydrogen atoms.

To avoid interference and improve the quality of the radio frequency
signal, the patient is placed inside a narrow tube encompassed by the
coil and scanning unit.

```{figure} images/rm_ge.jpg
:name: mri_equipment
:align: center

Magnetic resonance imaging equipment -
www.gehealthcare.com
```

```{figure} images/bobina.jpg
:name: philips_coil
:align: center

Coil - www.healthcare.philips.com
```
### Software and Hardware Requirements

InVesalius is designed to run on personal computers, such as desktops
and notebooks. Currently, it is compatible with the following operating
systems:

-   Microsoft Windows (Windows 7, 8, 10)

-   GNU/Linux (Ubuntu, Mandriva, Fedora)

-   Apple macOS

However, Windows offers the most stable performance and the easiest setup.  
The performance of InVesalius depends mainly on the number of
reconstructed slices (images offered by the software), the amount of
random access memory (RAM) available, the processor clock rate &
frequency, and operating system architecture (32-bit or 64-bit).

It is important to note that, as a general rule, the greater the amount
of RAM available on the system, the larger the number of slices that
can be opened simultaneously. For example, with 1 GB of available
memory, it can open about 300 slices with a resolution of 512x512
pixels. With 4 GB of memory, around 1000 images can be opened
simultaneously at the same resolution.

#### Minimum Computer Settings

-   32-bit Operating System

-   Intel Pentium 4 or equivalent 1.5 GHz

-   1 GB of RAM

-   10 GB available hard disk space

-   Graphics card with 64 MB memory

-   Video resolution of 1024x768 pixels

#### Recommended Computer Settings

-   64-bit Operating System

-   Intel i7 or equivalent processor

-   16 GB of RAM

-   20 GB available hard disk space

-   Geforce or AMD or Quadro (P2000 equivalent or superior) graphics card

-   Video resolution of 1920x1080 pixels

#### Hardware Components for Navigated TMS Users

The recommended hardware components for navigated TMS users are listed below.

InVesalius supports multiple different tracking devices, but 
using NDI cameras (either Vega or Lyra) is recommended.
To read more about which tracking device to choose,
please check the [tracking devices wiki page](https://github.com/invesalius/invesalius3/wiki/Which-tracking-device-to-choose).
In addition to the components below, [TMS accessories made by Brainbox](https://www.brainbox.shop/categories/brainsight-accs/1938652000002129022)
are also compatible with InVesalius.


| **Part**                             | **Requirements**                                                                                                                                                                                                                                                                                                                                                                                                      | **Information**                                                                                                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMS – Neuronavigation Trigger Cables | [BNCT shape adapter](https://www.amazon.de/-/en/Shape-Double-Female-Coaxial-Adapter/dp/B00L9X74WO/ref=sr_1_6?crid=2PJP0S4XSRNUW&amp;keywords=bnc+splitter+cable&amp;qid=1688046287&amp;sprefix=bnc+splitter+cable%2Caps%2C275&amp;sr=8-6)                                                                                                                                                                             | The trigger from TMS is connected to BNC adapter, which connects to BNC to squared pins, which connect to jumper wires, which connect to the USB trigger cable. |
|                                      | [2 x BNC to squared pins](https://fi.farnell.com/hirschmann-testmeasurement/933844001/test-lead-1-2m-60v/dp/4017468?st=bnc%20pin)                                                                                                                                                                                                                                                                                     |                                                                                                                                                                 |
|                                      | [Farnell Trigger cable (USB) - USB to TTL -232RG-VSW5V-WE](https://fi.farnell.com/ftdi/ttl-232rg-vsw5v-we/cable-ttl-usb-conv-wire-end-5v/dp/2352003?st=usb%20ttl) OR [Amazon - USB to TTL -PL2303HX](https://www.amazon.de/-/en/Candeon-PL2303HX-Upgrade-Converter-Download/dp/B08XXXXZRZ/ref=sr_1_19?crid=12YYDRV8BDPR8&amp;keywords=USB+TTL+cable&amp;qid=1688045214&amp;sprefix=usb+ttl+c%2Caps%2C313&amp;sr=8-19) | The Farnell cable is recommended. The Amazon cable might have a more complicated setup process.                                                                 |
|                                      | [4 x Jumper wires, 100 mm long or shorter](https://www.amazon.de/-/en/Bestlus-Breadboard-Exclusive-Bridges-Raspberry/dp/B09H2TRZHB/ref=sr_1_2?crid=2DOXQMSMQTFAG&amp;keywords=arduino+cables+100mm&amp;qid=1688048428&amp;sprefix=arduino+cables+100mm%2Caps%2C271&amp;sr=8-2)                                                                                                                                        |                                                                                                                                                                 |
| Tracking camera                      | [Polaris Vega ST Position Sensor, EPV, PL, CFR008](https://www.ndigital.com/optical-measurement-technology/polaris-vega/)                                                                                                                                                                                                                                                                                             |                                                                                                                                                                 |
|                                      | Polaris Vega PoE Midspan Power Supply 55 VDC 36W, 802.3 at compliant                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                 |
|                                      | Cable Assy - Ethernet 3.0 CAT 6 RJ45 to RJ45 double shielded                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                 |
|                                      | Polaris Vega Tool Kit, Passive                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                 |
|                                      | Camera stand                                                                                                                                                                                                                                                                                                                                                                                                          | The stand should offer possibility to move the camera around. Can be mounted in the wall, or a ceiling, or on a movable stand.                                  |
| Probe                                | 3D models provided by Renan or Aalto,                                                                                                                                                                                                                                                                                                                                                                                 | ROM file required.                                                                                                                                              |
|                                      | OR the NDI toolkit probe,                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                 |
|                                      | OR one existing from another navigations software.                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                 |
| Coil marker                          | Marker for the coils with attachment (a 3D model provided by Renan),                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                 |
|                                      | OR a clip mount designed by Renan.                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                 |
| Head marker                          | Head marker (a 3D model provided by Ana or Renan),                                                                                                                                                                                                                                                                                                                                                                    | Attach the marker by using a headband or by using a clip to connect it to safety glasses.                                                                       |
|                                      | OR a Polaris Tool Kit marker.                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                 |
| Pedal                                | [Bewinner USB Triple Foot Pedal](https://www.amazon.de/-/en/gp/product/B09ZR7FV3R/ref=ox_sc_act_title_3?smid=A2KREUBK79VF64&th=1)                                                                                                                                                                                                                                                                                     |                                                                                                                                                                 |
|                                      | [USB Extension cable 3 m](https://www.amazon.de/-/en/gp/product/B09GVGFBG5/ref=ox_sc_act_title_2?smid=A3QP6MATKOCSJT&th=1)                                                                                                                                                                                                                                                                                            |                                                                                                                                                                 |
|                                      | [4-Port USB 3.0 Hub](https://www.amazon.de/-/en/3-0-Hub-MacBook-Windows-Ultrabooks-Compatible/dp/B00Y211AFM/ref=sr_1_6?crid=1YDVTJXIW4HZI&keywords=usb+hub&qid=1692631216&refinements=p_72%3A419117031&rnid=419116031&sprefix=usb+hu%2Caps%2C195&sr=8-6)                                                                                                                                                              |                                                                                                                                                                 |



## Installation

To download InVesalius, visit one of the following sites:

* [InVesalius GitHub](http://invesalius.github.io),
* [Gov.br](https://www.cti.gov.br/invesalius).

### MS-Windows

To install InVesalius on MS-Windows, simply run the installer program.
When a window asking you to confirm the file execution appears, click
**Yes**.

```{figure} images/invesalius_screen/installation_exec_en.png
:name: installation_exec
:align: center

```

A new window will ask you to select the language of the installer.
Select the language and click **OK**.

```{figure} images/invesalius_screen/installation_select_language_en.png
:name: installation_select_language
:align: center

```

The Setup installer will appear. Click **Next**.

```{figure} images/invesalius_screen/installation_welcome_en.png
:name: installation_welcome
:align: center

```

Select **I accept the agreement** and click the **Next** button.

```{figure} images/invesalius_screen/installation_license_en.png
:name: installation_license
:align: center

```

Select the preferred destination for the InVesalius program files, then
click **Next**.

```{figure} images/invesalius_screen/installation_folder_en.png
:name: installation_folder
:align: center

```

Click the **Next** button.

```{figure} images/invesalius_screen/installation_program_name_en.png
:name: installation_program_name
:align: center

```

Select **Create a desktop shortcut** and click **Next**.

```{figure} images/invesalius_screen/installation_desktop_shortcut_en.png
:name: installation_desktop_shortcut
:align: center

```

Click the **Install** button.

```{figure} images/invesalius_screen/installation_resume_en.png
:name: installation_resume
:align: center

```

While the software is being installed, a progress window will appear.

```{figure} images/invesalius_screen/installation_progress_en.png
:name: installation_progress
:align: center

```

To run InVesalius after installation, check **Launch InVesalius 3.1** and
click the **Finish** button.

```{figure} images/invesalius_screen/installation_finish_en.png
:name: installation_finish
:align: center

```

When being run for the first time, a window will appear to select the
InVesalius language. Select the desired language and click **OK**.

```{figure} images/invesalius_screen/invesalius_language_select_en.png
:name: invesalius_language_select
:align: center

```

While InVesalius is loading, the opening window shown below will be
displayed.

```{figure} images/icons/splash_en.png
:name: splash
:align: center

```

The main program window will then open, as shown below.

```{figure} images/invesalius_screen/main_window_without_project_en.png
:name: main_window_without_project
:align: center

```
  

### MacOS

To start the installation on macOS, double-click the installer with
the left mouse button to begin installation.

```{figure} images/invesalius_screen/mac2.png
:name: mac2
:align: center

```

Hold down the left button on the InVesalius software icon and drag it to
the Applications folder. Both are contained in the installer.

The software is now installed and can be accessed through the menu.

## Image Import

InVesalius imports files in DICOM format, including compressed files
(lossless JPEG), Analyze (Mayo Clinic©), NIfTI, PAR/REC,
BMP, TIFF, JPEG and PNG formats.

### DICOM

Under the File menu, click on Import DICOM or use the shortcut Ctrl+I.
Additionally, DICOM files can be imported by clicking on the icon shown
in {numref}`dicom_import`.

```{figure} images/icons/file_import_original.png
:name: dicom_import
:align: center

Shortcut to DICOM import
```

Select the directory containing the DICOM files, as in
{numref}`win_folder`. InVesalius will search for files also in
subdirectories of the chosen directory if they exist.

Once the directory is selected, click **OK**.

```{figure} images/invesalius_screen/import_select_folder_en.png
:name: win_folder
:align: center

Folder selection
```

While InVesalius search for DICOM files in the directory, the loading
progress of the scanned files is displayed, as shown in the
{numref}`win_import_file`.

```{figure} images/invesalius_screen/import_load_files_en.png
:name: win_import_file
:align: center

Loading file status
```

If DICOM files are found, a window open (shown
{numref}`win_import_window`) will open to select the patient and
respective series to be opened. It is also possible to skip images for
reconstruction.

```{figure} images/invesalius_screen/import_window_en.png
:name: win_import_window
:align: center

Import window
```

To import a series with all images present, click \"**+**"\ on the
patient's name to expand the corresponding series. Double-click on the
description of the series. See
{numref}`import_serie`.

```{figure} images/invesalius_screen/import_window_detail_en.png
:name: import_serie
:align: center

Series selection
```

In some cases, when there is no computer with memory and/or satisfactory
processing to work with large numbers of images in a series, it is
recommended to skip some of them. To do this, click **once** with the
**left** mouse button over the description of the series
({numref}`import_serie`) and select how many images will be
skipped ({numref}`skip_image`), then click **Import**.

```{figure} images/invesalius_screen/import_window_skip_slice_en.png
:name: skip_image
:align: center

Skip image option
```

If there is an insufficient amount of available memory at the time of
loading the images, it is recommended that the resolution of the slices
be reduced to work with volumetric and surface visualization, as shown
in {numref}`resize_image`. The slices will be resized according to
the percentage relative to the original resolution. For example, if each
slice of the exam the dimension of 512 x 512 pixels and the \"Percentage
of original resolution\" is suggested to be 60 %, each resulting image
will be 307 x 307 pixels. To open with the original pixel resolution,
set the percentage to 100.

```{figure} images/invesalius_screen/import_window_lower_memory_en.png
:name: resize_image
:align: center

Image size reduction
```

If the image was obtained with the gantry tilted, it will be necessary to
correct to avoid distortion of any reconstruction. InVesalius allows the
user to do this easily. When importing an image with the gantry tilted a
dialog will appear, showing the gantry tilt angle.
({numref}`gantry_tilt`). It is possible to change this value, but
it is not recommended. Click on the **Ok** to do the correction. If you
click on the **Cancel** button, the correction will not be done.

```{figure} images/invesalius_screen/window_gantry_tilt_en.png
:name: gantry_tilt
:align: center

Gantry tilt correction
```

After the above procedure, a window will be displayed ({numref}`prog_recons`) with reconstruction 
(when images are stacked and interpolated).

```{figure} images/invesalius_screen/import_window_progress_en.png
:name: prog_recons
:align: center

Reconstruction progress
```

### Analyze

To import Analyze files, under the **File** menu, click **Import other
files**, then click on the **Analyze** option as show the
{numref}`analyze_menu`.

```{figure} images/invesalius_screen/import_analyze_menu_en.png
:name: analyze_menu
:align: center

Menu for importing images in analyze format.
```

Select the Analyze file format (**.hdr**) and click on **Open**
({numref}`analyze_import`).

```{figure} images/invesalius_screen/import_analyze_window_en.png
:name: analyze_import
:align: center

Import analyze file format.
```

### NIfTI

To import NIfTI files, under the **File** menu, click **Import other
files** and then click **NIfTI** as shown in
{numref}`import_nifti_menu_pt`.

```{figure} images/invesalius_screen/import_nifti_menu_en.png
:name: import_nifti_menu_pt
:align: center

Menu to import images in NIfTI format
```

Select the NIfTI file format (either **nii.gz** or **.nii**) then click
**Open**
({numref}`import_nifti_window_pt`). If the file is in another
format as **.hdr**, select **all files(\*.\*)** option.

```{figure} images/invesalius_screen/import_nifti_window_en.png
:name: import_nifti_window_pt
:align: center

Importing images in NIfTI format.
```

### PAR/REC

To import PAR/REC file, under the **File** menu, click **Import other
files**, and then click on **PAR/REC** as shown in
{numref}`import_parrec_menu_pt`.

```{figure} images/invesalius_screen/import_parrec_menu_en.png
:name: import_parrec_menu_pt
:align: center

Menu for importing PAR/REC images
```

Select PAR/REC file type with the file extension **.par** and click
**Open**
({numref}`import_parrec_window_pt`). If the file has no extension,
select **all files(\*.\*)** option.

```{figure} images/invesalius_screen/import_parrec_window_en.png
:name: import_parrec_window_pt
:align: center

PAR/REC import
```

### TIFF, JPG, BMP, JPEG or PNG (micro-CT)

TIFF, JPG, BMP, JPEG or PNG file format for microtomography equipment
(micro-CT or µCT) or others. InVesalius imports files in these
formats if pixels present are represented in **grayscale**.

To import, click on menu **File**, **Import other files\...** and then
click on **TIFF, JPG, BMP, JPEG or PNG (µCT)** option as shown in the
{numref}`import_bmp_menu_pt`.

```{figure} images/invesalius_screen/import_bmp_menu_en.png
:name: import_bmp_menu_pt
:align: center

Import images in BMP and others formats
```

Select the directory that contains the files, as shown the
{numref}`import_bmp_select_folder`. InVesalius will search for
files also in subdirectories of the chosen directory if they exist.

Click on **OK**.

```{figure} images/invesalius_screen/import_bmp_select_folder_en.png
:name: import_bmp_select_folder
:align: center

Folder selection
```

While InVesalius is looking for TIFF, JPG, BMP, JPEG, or PNG files in
the directory, the upload progress of the scanned files is displayed, as
illustrated in
{numref}`import_bmp_load_pt`.

```{figure} images/invesalius_screen/import_bmp_load_en.png
:name: import_bmp_load_pt
:align: center

Checking and loading files status.
```

If files in the desired formats are located, a window will open (shown
in {numref}`import_bmp_window_pt`) to display the files eligible for
reconstruction. Images can also be skipped to remove files from the
rebuild list. The files are sorted according to file names. It is
recommended that the files are numbered according to the desired rebuild
order.

```{figure} images/invesalius_screen/import_bmp_window_en.png
:name: import_bmp_window_pt
:align: center

Window to import BMP files.
```

To delete files that are not of interest, select a file by clicking the
left mouse button and then pressing the delete key. You can also choose
a range of files to delete by clicking the **left mouse button** on a
file, holding down the **shift** key, clicking again with the mouse
button in the last file of the track and finally pressing the **delete**
button.

Similar to when importing DICOM files, you can skip BMP images for
re-building. In some cases, particularly where a computer with
satisfactory memory and/or processing is unavailable, it may be
advisable to skip some of them to retain adequate program functionality.
To do this, select how many images to skip
({numref}`import_bmp_skip_pt`), then click **Import**.

```{figure} images/invesalius_screen/import_bmp_skip_en.png
:name: import_bmp_skip_pt
:align: center

Importation window
```

To reconstruct files of this type, a project name must be defined to
indicate the orientation of the images (axial, coronal or sagittal),
voxel spacing (*X*, *Y* and *Z*) in **mm** as shown in the
{numref}`import_bmp_spacing_pt`. The voxel spacing in *X* is the
pixel width of each image, *Y* the pixel length, and *Z* represents the
distance of each slice (voxel height).

If the image set consists of microtomography images, more specifically
GE and Brucker equipment, it is possible that InVesalius will read the
text file with the acquisition parameters that normally stay in the same
folder as the images and automatically insert the spacing. This
verification can be done when the values of *X*, *Y* and *Z* are
different from \"1.00000000\", otherwise it is necessary to enter the
values of the respective spacing.

**Correct spacing is crucial for correctly importing objects in
InVesalius. Incorrect spacing will provide incorrect measurements.**

Once all parameters have been input, click **OK**.

```{figure} images/invesalius_screen/import_bmp_spacing_en.png
:name: import_bmp_spacing_pt
:align: center

Import screen
```

If insufficient memory is available when loading images, it is
recommended to reduce the resolution of the slices to work with
volumetric and surface visualization, as shown in
{numref}`import_bmp_resize_pt` window.The slices will be resized
according to the percentage relative to the original resolution. For
example, if each slice of the exam contains the dimension of 512 x 512
pixels and the \"Percentage of the original resolution\" is suggested at
60, each resulting image will have 307 x 307 pixels. If you want to
open with the original resolution, set the percentage to 100.

```{figure} images/invesalius_screen/import_window_lower_memory_en.png
:name: import_bmp_resize_pt
:align: center

Image resize
```

After the previous steps, wait a moment for the program to complete the
multiplanar reconstruction as shown in
{numref}`import_bmp_mpr_pt`.

```{figure} images/invesalius_screen/import_window_progress_en.png
:name: import_bmp_mpr_pt
:align: center

Multiplanar reconstruction in progress.
```

## Image Adjustment

InVesalius cannot guarantee the correct image order; images may contain
incorrect information, or do not follow the DICOM standard. Therefore,
it is recommended to check if a lesion or an anatomical mark is on the
correct side. If not, it is possible to use the flip image or swap axes
tools. For image alignment, the rotation image tool can be used.

It is possible to mirror the image. To do so, select the **Tools** menu,
click **Image**, then **Flip** and click on one of the following options
({numref}`menu_img_mirroring_axis_pt`):

-   Right - Left

-   Anterior - Posterior

-   Top - Bottom

```{figure} images/invesalius_screen/menu_img_mirroring_axis_en.png
:name: menu_img_mirroring_axis_pt
:align: center

Menu to activate flip image tool.
```

{numref}`mirror_axial` and {numref}`mirror_axial_mirrored` show a comparison between the input image and
the flipped image. All other orientations are also modified when the
image is flipped.

```{figure} images/invesalius_screen/mirror_axial.png
:name: mirror_axial
:align: center

The image before mirroring.
```
```{figure} images/invesalius_screen/mirror_axial_mirrored.png
:name: mirror_axial_mirrored
:align: center

The image after axial mirroring.
```


### Swap Axes

The swap axes tool changes the image orientation, in the case that the
image has been wrongly imported. To perform this, select the **Tools**
menu, click **Image**, then **Swap Axes** and click on one of the
following options
({numref}`menu_invert_axis`):

-   From Right-Left to Anterior-Posterior

-   From Right-Left to Top-Bottom

-   From Anterior-Posterior to Top-Bottom

The {numref}`invert_axis_axial`
and {numref}`invert_axis_axial_inverted` show an example of an
image with inverted axes.

```{figure} images/invesalius_screen/menu_invert_axis_en.png
:name: menu_invert_axis
:align: center

Menu to activate swap image tool.
```


```{figure} images/invesalius_screen/invert_axis_axial_en.png
:name: invert_axis_axial
:align: center

Images before swap axes - from Anterior-Posterior to Top-Bottom.
```


```{figure} images/invesalius_screen/invert_axis_axial_inverted_en.png
:name: invert_axis_axial_inverted
:align: center

Images after swap axes - from Anterior-Posterior to Top-Bottom.
```

### Reorient Image (Rotate)

If it is necessary to align the image with a certain point of reference,
e.g. anatomical marker, use the reorient image tool. To open this tool, 
select the **Tools** menu, click **Image**, then **Reorient Image**
({numref}`menu_img_reorient`).


```{figure} images/invesalius_screen/menu_img_reorient_en.png
:name: menu_img_reorient
:align: center

Menu to activate reorient image tool.
```

When this tool is activated, a window is opened
({numref}`image_reorient_window`) showing orientation and by how
many degrees the image was rotated.


```{figure} images/invesalius_screen/image_reorient_window_en.png
:name: image_reorient_window
:align: center

Window that shows the reorientation image parameters.
```

To start reorienting the image, define the interpolation method that
 will be applied after rotation, by default is tricubic interpolation.
The interpolation options are:

-   Nearest Neighbour

-   Trilinear

-   Tricubic

-   Lanczos

Then, select the rotation point by keeping the **left** mouse button
pressed between the two lines intersecting
({numref}`image_reorient_adjust_center`) at one orientation, e.g.
axial, coronal or sagittal, and **drag** to the desired point.


```{figure} images/invesalius_screen/image_reorient_adjust_center_en.png
:name: image_reorient_adjust_center
:align: center

Defining the axis of rotation of the image.
```

To rotate the image, it is necessary to keep the **left** mouse button
pressed and **drag** until the reference point or anatomical marker
stays aligned with one of the lines
({numref}`image_reorient_rotated`). After the image is in the
desired position, click **Apply** in the parameter window
({numref}`image_reorient_window`). This may take a few moments
depending on the image size.
{numref}`image_reorient_rotated_applied` shows an image
successfully reoriented.


```{figure} images/invesalius_screen/image_reorient_rotated_en.png
:name: image_reorient_rotated
:align: center

Rotated image.
```


```{figure} images/invesalius_screen/image_reorient_rotated_applied_en.png
:name: image_reorient_rotated_applied
:align: center

Rotated image after reorientation is done.
```

## Image Manipulation (2D)

### Multiplanar Reconstruction

When images are imported, InVesalius automatically shows its multiplanar
reconstruction in the Axial, Sagittal and Coronal orientations, as well
as a window for 3D manipulation, as seen in
{numref}`mpr`.

```{figure} images/invesalius_screen/multiplanar_mask_window_en.png
:name: mpr
:align: center

Multiplanar reconstruction
```

In addition to creating a multiplanar reconstruction, InVesalius
segments an image.
For example, soft tissue bones can be highlighted.
The highlight is represented by the application of colors on a segmented
structure so that the colors form a mask over an image highlighting the
structure ({numref}`mpr`).This is discussed in more detail in the following
sections.

To hide the mask, use the data manager, located in the lower left corner
of the screen. Select the **Masks** tab and click once using the
**left** mouse button over the eye icon next to **\"Mask 1\"**, as shown
in {numref}`ger_masc`.


```{figure} images/invesalius_screen/data_mask_en.png
:name: ger_masc
:align: center

Mask manager
```

The eye icon disappears, and the colors of the segmentation mask are
hidden ({numref}`mpr_sem_mask`).


```{figure} images/invesalius_screen/multiplanar_window_en.png
:name: mpr_sem_mask
:align: center

Multiplanar reconstruction without segmentation mask
```

#### Axial Orientation

The axial orientation consists of cuts made transversally to the region
of interest, i.e. parallel cuts to the axial plane of the human body. In
{numref}`axial_corte`, an axial image of the skull region is
displayed.

```{figure} images/invesalius_screen/axial_en.png
:name: axial_corte
:align: center

Axial slice
```

#### Sagittal Orientation

The sagittal orientation consists of cuts made laterally in relation to
the region of interest, i.e. parallel cuts to the sagittal plane of the
human body, which divides it into the left and right portions. In
{numref}`sagittal_slice`, a sagittal skull image is displayed.

```{figure} images/invesalius_screen/sagital_en.png
:name: sagittal_slice
:align: center

Sagittal slice
```

#### Coronal Orientation

The coronal orientation is composed of cuts parallel to the coronal
plane, which divides the human body into ventral and dorsal halves. In
{numref}`coronal_slice` is displayed a skull image in coronal
orientation.


```{figure} images/invesalius_screen/coronal_en.png
:name: coronal_slice
:align: center

Coronal slice
```

### Correspondence Between the Axial, Sagittal and Coronal Orientations

To find out the common point of intersection of the images in different 
orientations, simply activate the \"Slices cross intersection\" feature
with the shortcut icon located on the toolbar. See
{numref}`cross_icon`.

```{figure} images/icons/cross.png
:name: cross_icon
:align: center

Shortcut to show common point between different orientations.
```

When the feature is activated, two cross-sections that intersect
perpendicularly are displayed on each image
({numref}`cross_all`). The intersection point of each pair of
segments represents the common point between different orientations.

To modify the point, hold down the **left** mouse button and **drag**.
Automatically, the corresponding points will be updated in each image.

```{figure} images/invesalius_screen/multiplanar_window_cross_en.png
:name: cross_all
:align: center

Common point between differents orientations.
```

To deactivate the feature, simply click on the shortcut again
({numref}`cross_icon`). This feature can be used in conjunction
with the slice editor (which will be discussed later).

### Interpolation

By default, the 2D images visualization is interpolated
({numref}`axial_interpoleted`. To deactivate this feature, select the
**View** menu and select **Interpolated slices**
({numref}`menu_interpoleted_image_pt`). It will then be possible
to visualize each pixel individually as shown in
{numref}`axial_not_interpoleted`.

**This interpolation is for visualization purposes only, and does not
directly influence segmentation or 3D surface generation.**

```{figure} images/invesalius_screen/menu_interpoleted_image_en.png
:name: menu_interpoleted_image_pt
:align: center

Menu to disable and enable interpolation.
```

```{figure} images/invesalius_screen/axial_interpoleted.png
:name: axial_interpoleted
:align: center

Interpolated image visualization.
```

```{figure} images/invesalius_screen/axial_not_interpoleted.png
:name: axial_not_interpoleted
:align: center

Non-interpolated image visualization.
```

### Move

To move an image on the screen, use the Move shortcut icon on the
toolbar ({numref}`move_icon`). Click on the icon to activate, then with
the **left** mouse button on the image, it to the desired direction.
{numref}`move_img` shows a displaced (moved) image.

```{figure} images/icons/tool_translate_original.png
:name: move_icon
:align: center

Shortcut to move images.
```

```{figure} images/invesalius_screen/axial_pan_en.png
:name: move_img
:align: center

Displaced image.
```

### Rotate

Images can be rotated by using the Rotate shortcut on the toolbar
({numref}`rot_icon`). To rotate an image, click on the icon and
then with the **left** mouse button **drag** clockwise or anticlockwise
as required.

```{figure} images/icons/tool_rotate_original.png
:name: rot_icon
:align: center

Shortcut to rotate images.
```

```{figure} images/invesalius_screen/axial_rotate_en.png
:name: rotate_all
:align: center

Rotated image
```

### Zoom

In InVesalius, there are different ways to enlarge an image. You can
maximize the desired orientation window, apply zoom directly to the
image, or select the region of the image to enlarge. Each of these
methods is detailed below.

#### Maximizing Orientation Windows

The main InVesalius window is divided into 4 sub-windows: axial,
sagittal, coronal and 3D. Each of these can be maximized to occupy the
entire area of the main window. To do this, simply **left** mouse click
on the subwindow icon located in the **upper right corner**
({numref}`maximize_window`). To restore a maximized window to its
previous size, simply click the icon again.

```{figure} images/invesalius_screen/maximize_sagital_mpr.png
:name: maximize_window
:align: center

Detail of a sub-window (Note the maximize icon in the upper right corner).
```

#### Enlarging or Shrinking an Image

To enlarge or shrink an image, click on the zoom shortcut icon in the
toolbar ({numref}`zoom_icon`). Hold down the **left** mouse button on the
image and **drag** the mouse **up** to enlarge or **down** to shrink.

```{figure} images/icons/tool_zoom_original.png
:name: zoom_icon
:align: center

Zoom shortcut
```

#### Enlarging an Image Area

To enlarge a certain image area, click on the \"Zoom based on
selection\" icon in the toolbar
({numref}`zoom_icon_loc`). Position the mouse pointer at the
origin point of the selection, click and hold the **left** mouse button
and **drag** it to the end selection point to form a rectangle
({numref}`zoom_select`). Once the left mouse button is released,
the zoom operation will be applied to the selected region
({numref}`zoom_applied`).

```{figure} images/icons/tool_zoom_select_original.png
:name: zoom_icon_loc
:align: center

Zoom based on selection shortcut.
```

```{figure} images/invesalius_screen/tool_zoom_select_image_en.png
:name: zoom_select
:align: center

Area selected for zoom.
```

```{figure} images/invesalius_screen/tool_image_with_zoom_en.png
:name: zoom_applied
:align: center

Enlarged image.
```

(brightness-and-contrast-windows)=
### Brightness and Contrast (Windows)

To improve image visualization, the *window width* and *window level*
features can be used; these are more commonly known as *brightness and
contrast* or *window* (for radiologists). With this feature, it is
possible to set the range of the gray scale (*window level*) and the
width of the scale (*window width*) to be used to display the images.

The feature can be activated by the \"Brightness and Contrast\" shortcut
icon in the toolbar. See
{numref}`window_level_shortcut`.

```{figure} images/icons/tool_contrast_original.png
:name: window_level_shortcut
:align: center

Brightness and contrast shortcut
```

To increase the brightness, hold down the **left** mouse button and
**drag** horizontally to the right. To decrease the brightness, simply
drag the mouse to the left. The contrast can be changed by dragging the
mouse (with the **left** button pressed) vertically: up to increase, or
down to decrease contrast.

To deactivate the feature, click again on the shortcut icon
({numref}`window_level_shortcut`).

Preset brightness and contrast patterns may be used with InVesalius.
The table below lists some tissue types with their
respective brightness and contrast values. To use the presets, position
the mouse cursor over an image and **right-click** to open a context
menu, then select **Window width and level**, and click on the preset
option according to the tissue type, as shown in
{numref}`window_level`.

```{figure} images/invesalius_screen/menu_window_and_level_en.png
:name: window_level
:align: center

Context menu for brightness and contrast selection
```

**Brightness and contrast values for some tissues**

| Tissue                        | Brightness | Contrast |
|-------------------------------|------------|----------|
| Default                       | Exam       | Exam     |
| Manual                        | Changed    | Changed  |
| Abdomen                       | 350        | 50       |
| Bone                          | 2000       | 300      |
| Brain                         | 80         | 40       |
| Brain posterior fossa         | 120        | 40       |
| Contour                       | 255        | 127      |
| Emphysema                     | 500        | -850     |
| Ischemia - Hard, non-contrast | 15         | 32       |
| Ischemia - Soft, non-contrast | 80         | 20       |
| Larynx                        | 180        | 80       |
| Liver                         | 2000       | -500     |
| Lung - Hard                   | 1000       | -600     |
| Lung - Soft                   | 1600       | -600     |
| Mediastinum                   | 350        | 25       |
| Pelvis                        | 450        | 50       |
| Sinus                         | 4000       | 400      |
| Vasculature - Hard            | 240        | 80       |
| Vaculature - Soft             | 680        | 160      |


### Pseudo Color

Another feature to improve the visualization of the images is the pseudo
color. This replaces gray levels by color, or by inverted gray levels.
In the latter case, previously clear regions of the image become darker
and vice versa.

To change the view using a pseudo color, position the mouse cursor over
the image and **right-click** to open a context menu on it. When the
menu opens, select the entry **Pseudo color**, and then click on the
desired pseudo color option, as shown in
{numref}`pseudo_color`.

```{figure} images/invesalius_screen/pseudo_menu_en.png
:name: pseudo_color
:align: center

Pseudo color
```

[Figures](#pseudo_default) below demonstrate the various pseudo color
options available.

```{figure} images/invesalius_screen/pseudo_default.jpg
:name: pseudo_default
:align: center

Default pseudo color.
```

```{figure} images/invesalius_screen/pseudo_desert.jpg
:name: pseudo_desert
:align: center

Desert pseudo color.
```

```{figure} images/invesalius_screen/pseudo_hue.jpg
:name: pseudo_hue
:align: center

Hue pseudo color.
```

```{figure} images/invesalius_screen/pseudo_inverse.jpg
:name: pseudo_inverse
:align: center

Inverse pseudo color.
```

```{figure} images/invesalius_screen/pseudo_ocean.jpg
:name: pseudo_ocean
:align: center

Ocean pseudo color.
```

```{figure} images/invesalius_screen/pseudo_rainbow.jpg
:name: pseudo_rainbow
:align: center

Rainbow pseudo color.
```

```{figure} images/invesalius_screen/pseudo_saturation.jpg
:name: pseudo_saturation
:align: center

Saturation pseudo color.
```

### Projection Type

It is possible to change the projection type of the 2D images, in
addition to the normal mode, InVesalius has six types of projections
that can be accessed as follows: Place the mouse over the image and
**right-click** to open a context menu on it. When the menu opens,
select the projection type option, and then click on the desired
projection option, as shown in the
{numref}`menu_proj`.

```{figure} images/invesalius_screen/menu_projection_en.png
:name: menu_proj
:align: center

Projection type menu
```

#### Normal

Normal mode is the default view, showing the unmodified image as it was
when acquired or customized previously with either brightness and
contrast or pseudo color. Normal mode is shown below in
{numref}`proj_normal`.

```{figure} images/invesalius_screen/multiplanar_window_en.png
:name: proj_normal
:align: center

Normal projection
```

(maxip)=
#### MaxIP

MaxIP is also known as MIP (*Maximum Intensity Projection*). MaxIP
selects only voxels that have maximum intensity among those visited as
shown in {numref}`proj_maxip`. According to the amount of, or \"depth\" of
MaxIP, each voxel is visited in order of overlap, for example, to select
MaxIP of the pixel (0, 0) consisting of 3 slices it is necessary to
visit pixel (0, 0) of slices (1, 2, 3) and select the highest value.

```{figure} images/invesalius_screen/multiplanar_window_maxip_en.png
:name: proj_maxip
:align: center

MaxIP projection
```

As shown in {numref}`proj_maxip_qtd`, the number of MaxIP images is set at
the bottom of each orientation image.

```{figure} images/invesalius_screen/multiplanar_window_maxip_number_en.png
:name: proj_maxip_qtd
:align: center

Selection the amount of images that composes the MaxIP or MIP
```

#### MinIP

Unlike MaxIP, MinIP (*Minimum Intensity Projection*) selects only the
voxels that have minimal intensity among those visited, as shown in
{numref}`proj_minIP`. The image number selection comprising the
projection is made at the bottom of each orientation image as shown in
{numref}`proj_maxip_qtd`.


```{figure} images/invesalius_screen/multiplanar_window_minip_en.png
:name: proj_minIP
:align: center

MinIP projection
```

#### MeanIP

The MeanIP (*Mean Intensity Projection*) technique which is shown in the
{numref}`proj_meanIP` composes the projection by averaging voxels
visited in the same way as the MaxIP and MinIP methods. It is also
possible to define how many images will compose the projection at the
bottom of the image of each orientation as shown in
{numref}`proj_maxip_qtd`.

```{figure} images/invesalius_screen/multiplanar_window_mean_en.png
:name: proj_meanIP
:align: center

MeanIP projection
```

(mida)=
#### MIDA

The MIDA (*Maximum Intensity Difference Accumulation*) technique
projects an image taking into account only voxels that have local
maximum values. From each pixel a ray is simulated towards the volume,
with each voxel being intercepted by each ray reaching the end of the
volume. Each of the voxels visited has its accumulated value, but are
taken into account only if the value is greater than previously visited
values. Like MaxIP, one can select how many images are used to
accumulate the values.
{numref}`proj_MIDA` shows an example of MIDA projection.

```{figure} images/invesalius_screen/multiplanar_window_mida_en.png
:name: proj_MIDA
:align: center

MIDA projection
```

As {numref}`proj_MIDA_inv` shows, it is possible to invert the order
that the voxels are visited by selecting the **Inverted order** option
in the lower corner of the screen.

```{figure} images/invesalius_screen/multiplanar_window_mida_inverted_en.png
:name: proj_MIDA_inv
:align: center

Inverted order MIDA projection
```

#### Contour MaxIP

The Contour MaxIP function consists of visualizing contours present in
the projection generated with MaxIP
technique ([MaxIP](#maxip)). An example is presented in
{numref}`proj_contorno_maxip`.

```{figure} images/invesalius_screen/multiplanar_window_contour_maxip_en.png
:name: proj_contorno_maxip
:align: center

Contour MaxIP projection
```

#### Contour MIDA

The Contour MIDA function consists of visualizing contours present in
the projection generated with the MIDA
technique ([MIDA](#mida)). Like MIDA, you can reverse the order that the
volume is visited, as shown in
{numref}`proj_contorno_mida`.

```{figure} images/invesalius_screen/multiplanar_window_contour_mida_en.png
:name: proj_contorno_mida
:align: center

Contour MIDA projection
```

## Segmentation

To select a certain type of tissue from an image, it is used the
segmentation feature at InVesalius.

### Threshold

When using the thresholding segmentation technique, only the pixels
whose intensity is inside the threshold range defined by the user are
detected. The threshold is defined by two values, the initial (minimum)
and final (maximum) threshold.

In thresholding segmentation technique only the *pixels* whose intensity
is inside threshold range defined by the user. The Threshold is defined by
two numbers, the initial and final thresholds, also known as the minimum and
maximum thresholds. 

Thresholding segmentation is located on the InVesalius left-panel, item
**2. Select region of interest**
({numref}`region_selection`).

```{figure} images/invesalius_screen/segmentation_threshold_window_left_en.png
:name: region_selection
:align: center

Select region of interest -threshold.
```

Before starting a segment, it is necessary to configure a mask. A mask is
an image over to examine an image where the selected regions are colored
({numref}`region_selection_masc`).

```{figure} images/invesalius_screen/segmentation_threshold_axial_en.png
:name: region_selection_masc
:align: center

Mask - selected region in yellow.
```

To change the threshold, use the image greyscale control
({numref}`region_selection_bar`). Move the *left* sliding control
to change the initial threshold. Move the **right** sliding control to
change the final threshold. It is also possible to input the desired
threshold values in the text boxes in the left and right side of the
thresholding control. The mask will be automatically updated when the
thresholding values are changed, showing in color the pixels inside the
thresholding range.

```{figure} images/invesalius_screen/segmentation_threshold_bar.png
:name: region_selection_bar
:align: center

Selecting *pixels* with intensity between 226 and 3021 (Bone).
```

It is also possible to select some predefined thresholding values based
on some type of tissues, like those displayed in
{numref}`limiar_presets`. Just select the desired tissue and the
mask will automatically update.

```{figure} images/invesalius_screen/segmentation_threshold_presets_en.png
:name: limiar_presets
:align: center

Selection list with some predefined thresholding values.
```

The table below shows thresholding values according to tissues and materials. The table
indicates images obtained from medical tomographs. The range of gray
values from images obtained from odontological tomographs is greater
and non-regular. Thus, it is necessary to use sliding controls
({numref}`region_selection_bar`) to adjust the thresholding
values.

**Table - Predefined thresholding values to some materials**

| Material              | Initial threshold | Final threshold |
|-----------------------|-------------------|-----------------|
| Bone                  | 226               | 3021            |
| Compact Bone (Adult)  | 662               | 1988            |
| Compact Bone (Child)  | 586               | 2198            |
| Custom                | User Def.         | User Def.       |
| Enamel (Adult)        | 1553              | 2850            |
| Enamel (Child)        | 2042              | 3021            |
| Fat Tissue (Adult)    | -205              | -51             |
| Fat Tissue (Child)    | -212              | -72             |
| Muscle Tissue (Adult) | -5                | 135             |
| Muscle Tissue (Child) | -25               | 139             |
| Skin Tissue (Adult)   | -718              | -177            |
| Skin Tissue (Child)   | -766              | -202            |
| Soft Tissue           | -700              | 225             |
| Spongial Bone (Adult) | 148               | 661             |
| Spongial Bone (Child) | 156               | 585             |


To create a new mask, click **Create new mask**
({numref}`shortcut_new_mask`). Then, click **Select region of
interest**.

```{figure} images/icons/object_add_original.png
:name: shortcut_new_mask
:align: center

Button to create a new mask.
```

After clicking on this button, a dialog will be shown
({numref}`create_new_mask`). Select the desired threshold and
click on **Ok**.

```{figure} images/invesalius_screen/segmentation_threshold_window_dialog_en.png
:name: create_new_mask
:align: center

Creating a new mask.
```

After segmentation, it is possible to generate a corresponding 3D
surface. The surface is formed by triangles. The following chapter will
give more details about surfaces.

Click on the **Create surface** button
({numref}`generate_surface`) to create a new surface. If there is
a surface created, previously you may overwrite it with the new one. To
do this, select the option **Overwrite last surface** before creating the
new surface.

```{figure} images/invesalius_screen/segmentation_generate_surface_en.png
:name: generate_surface
:align: center

Create surface button.
```

After a few moments the surface will be displayed at the 3D
visualization window of InVesalius
({numref}`surface`).

```{figure} images/invesalius_screen/surface_from_threshold.png
:name: surface
:align: center

3D surface.
```

### Manual Segmentation (Image edition)

Thresholding segmentation may not be efficient in some cases since it is
applied to the whole image. Manual segmentation may be used to segment
only an isolated region. Manual segmentation also allows users to add or
remove some image regions from the segmentation. To use it, click on
**Manual edition**
({numref}`advanced_edition`) to open the manual segmentation
panel.

```{figure} images/invesalius_screen/segmentation_manual_label_en.png
:name: advanced_edition
:align: center

Icon to open the Manual segmentation panel.
```

{numref}`edition_slices_ref` shows the Manual segmentation panel.

```{figure} images/invesalius_screen/segmentation_manual_window_en.png
:name: edition_slices_ref
:align: center

Manual segmentation panel.
```

There are two brushes used for segmentation: a circle and a square.
Click on the triangle icon (see
{numref}`brush_type`) to show brush types, then click on the
desired brush.

```{figure} images/invesalius_screen/segmentation_manual_pencil_type.png
:name: brush_type
:align: center

Brush types.
```

Brush sizes can also be adjusted, as shown in
{numref}`select_diameter`.

```{figure} images/invesalius_screen/segmentation_manual_diameter.png
:name: select_diameter
:align: center

Adjusting the brush size.
```

The following are available options when using brushes in InVesalius:

-   **Draw**: for adding a non-selected region to the segmentation;

-   **Erase**: for removal of a non-selected region;

-   **Threshold**: applies the thresholding locally, adding or removing
    a region inside or outside the threshold range.

{numref}`select_brush_operations` shows the available brush
operations.

```{figure} images/invesalius_screen/segmentation_manual_pencil_type_operation_type_en.png
:name: select_brush_operations
:align: center

Brush operations.
```

{numref}`noise_amalgaman` shows an image with noise caused by the
presence of a dental prosthesis. Note the rays emerging from the dental
arch: the thresholding segments the noise since its intensity is inside the threshold of bone.

```{figure} images/invesalius_screen/segmentation_manual_noise_amalgam.jpg
:name: noise_amalgaman
:align: center

Noisy image segmented with threshold.
```

{numref}`surface_amagaman` shows a surface created from that
segmentation.

```{figure} images/invesalius_screen/segmentation_manual_noise_amalgam_3d.jpg
:name: surface_amagaman
:align: center

Surface generated from noisy image.
```

```{figure} images/invesalius_screen/segmentation_manual_noise_amalgam_3d_zoom.jpg
:name: surface_amagaman_zoom
:align: center

Zoom in the noisy area.
```

In such cases, use the manual segmentation with the **erase** brush. Keep
the **left** mouse button pressed while dragging the brush over the
region to be removed (in mask).

{numref}`editor_amalgaman` shows the image from
{numref}`noise_amalgaman` after.

```{figure} images/invesalius_screen/segmentation_manual_noise_amalgam_removed.jpg
:name: editor_amalgaman
:align: center

After removing the noise.
```

```{figure} images/invesalius_screen/segmentation_manual_noise_amalgam_removed_3d_zoom.jpg
:name: surface_edited_amalgaman
:align: center

Surface generate after removing the noise.
```

A surface can be generated after manual segmentation
({numref}`surface_edited_amalgaman`). Since it was used in the
manual segmentation procedure, when clicking on Create surface button, a
dialog ({numref}`new_surface_edited`) will be opened to select if the
surface is created with the method **Binary** (blocky) or **Context
aware smoothing** (smoother).

```{figure} images/invesalius_screen/surface_generation_dialog_en.png
:name: new_surface_edited
:align: center

Surface creation methods.
```

### Watershed

In watershed segmentation, the user demarcates objects and background
detail. This method treats the image as watershed (hence the name) in
which the gray values (intensity) are the altitudes, forming valleys and
mountains. The markers are water source. The waters fill the watershed
until the waters gather together, thus distinguishing a background from
an object. To use Watershed segmentation, click on Watershed to open the
watershed panel
({numref}`watershed_panel`).

```{figure} images/invesalius_screen/segmentation_watershed_panel_en.png
:name: watershed_panel
:align: center

Watershed segmentation
panel.
```

Before segmenting to with Watershed, it is recommended to clean the mask
(see [Mask Cleaning](#mask-cleaning)).

To insert a marker (object or background), a brush is used, similar to
manual segmenting. You can use a circle or square brush and set its
size.

Select brush operations from the following:

-   **Object**: to insert object markers;

-   **Background**: to insert background markers (not object);

-   **Delete**: to delete markers.

The option **Overwrite mask** is used when the user wants the result of
watershed segmentation to overwrite the existing segmentation. The
option **Use WWWL** is used to make watershed take into account the
image with the values of window width and window level (not the raw
image) which may result in better segmentation.

Click on the button on the left side of the panel
({numref}`watershed_conf`) to access more watershed
configurations. This button will open a dialog
({numref}`watershed_janela_conf`). The method option allows 
choosing the Watershed algorithm to be used to segment. It may be the
conventional **Watershed** or **Watershed IFT**, which is based on the
IFT (*Image Forest Transform*) method. In some cases, like brain
segmentation, the **Watershed IFT** may have a better result.

The connectivity option refers to the pixel neighbourhood (4 or 8
when in 2D, or 6, 18 or 26 when in 3D). **Gaussian sigma** is a
parameter used in the smoothing algorithm (the image is smoothed before
the segmentation to remove the noise and get better results). The
greater this value, the smoother the image will be.

```{figure} images/icons/configuration.png
:name: watershed_conf
:align: center

Button to open the Watershed configuration
dialog.
```


```{figure} images/invesalius_screen/segmentation_watershed_conf_en.png
:name: watershed_janela_conf
:align: center

Watershed configuration
dialog.
```

Normally the **Watershed** is applied only in one slice, not in the
whole image. After adding the markers is possible to apply the watershed
to the whole image by clicking on the button **Expand watershed to 3D**.
{numref}`watershed_2d` shows the result of watershed segmentation
in a slice (2D) of brain image.

{numref}`watershed_3d` shows the segmentation expanded to the
whole image (3D).

{numref}`watershed_2d` also shows the object markers (in light
green), the background markers (in red) and the segmentation mask (in
green) overlaying the selected regions (result).

```{figure} images/invesalius_screen/segmentation_watershed_axial.png
:name: watershed_2d
:align: center

Watershed applied to a
slice.
```


```{figure} images/invesalius_screen/segmentation_watershed_multiplanar_3d_pt.png
:name: watershed_3d
:align: center

Brain segmentation using the watershed method applied to the whole
image (3D).
```

### Region Growing

Region growing tool is accessed in the menu **Tools**, **Segmentation**,
**Region growing**
({numref}`menu_segmentation_region_growing`). Before segmenting, 
select if the operation is in **2D - Actual slice** or **3D — All
slices**. It is also necessary to select the connectivity: 4 or 8 to
2D or 6, 18 or 26 to 3D. It's also necessary to select the method,
which may be **Dynamic, Threshold, or Confidence**
{numref}`segmentation_region_growing_dinamic`.


```{figure} images/invesalius_screen/menu_segmentation_region_growing_en.png
:name: menu_segmentation_region_growing
:align: center

Menu to access the region growing segmentation segmentation
tool.
```


```{figure} images/invesalius_screen/segmentation_region_growing_dinamic_en.png
:name: segmentation_region_growing_dinamic
:align: center

Dialog to configure the parameters of region growing segmentation
tool.
```

This segmentation technique starts with a pixel (indicated by the user
left-clicking with the mouse). The selection expands by analyzing the
neighborhood of the selected pixels and including those of a given set
of qualities. Each region-growing method has a different condition of
selection:

-   **Dynamic**: Uses the value of the pixel clicked by the user. Then
    every connected pixel inside the lower (min) and the upper (max)
    range deviation are selected. The option **Use WWWL** is default and
    takes into account the image with **window width** and **window
    level** applied not the raw one
    ({numref}`segmentation_region_growing_dinamic_parameter`).

```{figure} images/invesalius_screen/segmentation_region_growing_dinamic_parameter_en.png
:name: segmentation_region_growing_dinamic_parameter
:align: center

Dynamic method parameters.
```

-   **Threshold**: This method selects the pixels whose intensity are
    inside the minimum and maximum threshold
    ({numref}`segmentation_region_growing_limiar`).


```{figure} images/invesalius_screen/segmentation_region_growing_limiar_en.png
:name: segmentation_region_growing_limiar
:align: center

Adjust the threshold.
```

-   **Confidence**: This method starts by calculating the standard
    deviation and the mean value of the pixel selected by the user and
    its neighbourhood. Connected pixels with value inside the range
    (given by the mean more and less the standard deviation multiplied
    by the **Multiplier** parameter). It then calculates the mean and
    the standard deviation from the selected pixels, then carries out
    the expansion. This process is repeated according to the
    **Iterations** parameter.
    {numref}`segmentation_region_growing_confidence_parameter`
    shows the parameters for this method.


```{figure} images/invesalius_screen/segmentation_region_growing_confidence_parameter_en.png
:name: segmentation_region_growing_confidence_parameter
:align: center

Confidence parameter.
```

## Mask

### Boolean Operations

After segmenting, some boolean operations can be performed between
masks. The boolean operations supported by InVesalius are:

-   **Union**, perform union between two masks;

-   **Difference**, perform difference from the first mask to the second
    one;

-   **Intersection**, keeps what is common in both masks.

-   **Exclusive disjunction (XOR)**: keeps the regions of the first mask
    which are not in the second mask and regions from the second mask
    which are not in the first mask.

To use this tool, go to the **Tools**, menu, select **Mask**, and then
Boolean operations as shown in
{numref}`booleano_menu`. Select the first mask, the operation to
be performed and the second mask as shown in
{numref}`booleano_janela` then click **OK**.

```{figure} images/invesalius_screen/mask_operation_boolean_menu_en.png
:name: booleano_menu
:align: center

Menu to open boolean operations
tool.
```

```{figure} images/invesalius_screen/mask_boolean_dialog_en.png
:name: booleano_janela
:align: center

Boolean operations
tool.
```

[Figures](#booleano_disj_exc) below show some examples of 
boolean operations.

```{figure} images/invesalius_screen/booleano_disj_exc.png
:name: booleano_disj_exc
:align: center

```

```{figure} images/invesalius_screen/booleano_m_a.png
:name: booleano_m_a
:align: center

```

```{figure} images/invesalius_screen/booleano_uniao.png
:name: booleano_uniao
:align: center

```


(mask-cleaning)=
### Mask Cleaning

A mask can be cleaned, as shown in
{numref}`limpeza_mascara`. This is recommended before inserting
Watershed markers. This tool is located on the **Tools** menu. Select
**Mask**, then **Clean mask**, or use the shortcut **CTRL+SHIFT+A**.

```{figure} images/invesalius_screen/mask_clean_menu_en.png
:name: limpeza_mascara
:align: center

Mask
cleaning
```

### Fill Holes Manually

Segmentation may leave some unwanted holes. It's recommended to fill
them because the surface generated from this mask may have some
inconsistencies. To do this, access the menu **Tools**, **Mask**, **Fill
holes manually**
({numref}`menu_mask_manual_fill_holes`). A dialog window will be
shown
({numref}`mask_manual_fill_holes_window`) to configure the
parameters.


```{figure} images/invesalius_screen/menu_mask_manual_fill_holes_en.png
:name: menu_mask_manual_fill_holes
:align: center

Menu to access the tool to fill holes
manually.
```

```{figure} images/invesalius_screen/mask_manual_fill_holes_window_en.png
:name: mask_manual_fill_holes_window
:align: center

Dialog to configure the parameters of Fill holes manually
tool.
```

It is possible to fill hole on a mask slice (**2D - Actual slice**) or
on all slices, selecting the option (**3D - All slices**). The
connectivity may also be configured: 4 or 8 for 2D and 6, 18 and
26 for 3D.

After configuring the desired parameters, left-click on holes to fill
them. {numref}`mask_axial_with_hole` shows a mask with some holes and {numref}`mask_axial_filled_hole` 
the mask with the holes filled. 
Click on the close button or close the dialog to deactivate this tool.

```{figure} images/invesalius_screen/mask_axial_with_hole.png
:name: mask_axial_with_hole
:align: center

A mask with holes.
```

```{figure} images/invesalius_screen/mask_axial_filled_hole.png
:name: mask_axial_filled_hole
:align: center

A mask with filled holes.
```

### Fill Holes Automatically

To open this tool, go to the **Tools** menu, select **Mask** then **Fill
holes automatically**
({numref}`menu_mask_automatic_fill_holes`). This will open a
dialog to configure the parameters. This tool doesn't require the user
to click on the holes they desire to fill. This tool will fill the holes based
on the **max hole size parameter** given in number of voxels
({numref}`mask_automatic_fill_holes_window`).

```{figure} images/invesalius_screen/menu_mask_automatic_fill_holes_en.png
:name: menu_mask_automatic_fill_holes
:align: center

Menu to open the Fill holes automatically
tool.
```


```{figure} images/invesalius_screen/mask_automatic_fill_holes_window_en.png
:name: mask_automatic_fill_holes_window
:align: center

Dialog to configure the parameters used to fill the
holes.
```


Holes can also be filled on a mask slice (**2D - Actual slice**) or on
all slices, selecting the option (**3D - All slices**). The connectivity
will thus be 4 or 8 to 2D and 6, 18 and 26 to 3D. If 2D, the
user must indicate in which orientation window the holes will be filled.

After setting the parameters, click **Apply**. If the result is not
 suitable, set another hole size value or connectivity. Click **Close** to
close this tool.

### Remove Parts

After generating a surface, it is recommended to remove the unwanted
disconnected parts from a mask. This way, the surface generation will use
less RAM and make the process quicker. To remove any unwanted parts, go
to the **Tools** menu, select **Mask** and then **Remove Parts**
({numref}`menu_mask_remove_part`). A dialog will be shown to
configure the selection parameters
({numref}`mask_remove_parts_window`).

It's possible to select disconnected parts only on a mask slice (**2D -
Actual slice**) or on all slices (**3D - All slices**); users may also
configure the connectivity at the same time.


```{figure} images/invesalius_screen/menu_mask_remove_part_en.png
:name: menu_mask_remove_part
:align: center

Menu to open the Remove parts
tool.
```


```{figure} images/invesalius_screen/mask_remove_parts_window_en.png
:name: mask_remove_parts_window
:align: center

Dialog to configure the parameters used in Remove
parts.
```

After selecting the desired parameters, click with the **left-button** of
the mouse on the region you want to remove.
Click **Close** to stop using this
tool.


### Select Parts

To open the Select parts tool, access the **Tools** menu, select
**Mask** then **Select parts**
({numref}`menu_mask_select_part`). A dialog will be shown to
configure the name of the new mask and the connectivity (6, 18
or 26).

To select a region, **left-click** on a pixel; multiple regions can be
selected. The selected region(s) will be shown with a red mask. After
selecting all the wanted regions, click **OK** to create a new mask with
the selected regions.
{numref}`mask_selected_part_a` shows a region selected in red.
{numref}`mask_selected_part_b` shows the selected region in a new
mask.

```{figure} images/invesalius_screen/menu_mask_select_part_en.png
:name: menu_mask_select_part
:align: center

Menu to open the Select parts
tool.
```

```{figure} images/invesalius_screen/mask_select_part_en.png
:name: mask_select_part
:align: center

Dialog to configure the parameters of Select parts
tool.
```

```{figure} images/invesalius_screen/mask_axial_select_part_pt.png
:name: mask_selected_part_a
:align: center

Example of mask region selection.
```

```{figure} images/invesalius_screen/mask_axial_selected_part_pt.png
:name: mask_selected_part_b
:align: center

Final image with only the selected region
```


### Crop

The crop tool allows users to select and use a specific section of image
of interest. This may reduce the amount of information needed to be
processed when generating a surface. To open, access the **Tool** menu,
then **Mask** and **Crop**
({numref}`menu_mask_crop`).

```{figure} images/invesalius_screen/menu_mask_crop_en.png
:name: menu_mask_crop
:align: center

Menu open the Crop tool.
```

A box allowing for the selection of a specific area will then be
displayed.

(surface-triangle-mesh)=
## Surface (Triangle mesh)

InVesalius generates 3D surfaces based on image segmentation. A surface
is generated using the marching cubes algorithm by transforming voxels
from the stacked and segmented images to polygons (triangles in this
case).

The controls to configure a 3D surface are accessible on the left panel,
under **3. Configure 3D surface**, **Surface properties** you have the
controls to configure a 3D surface
({numref}`3d_surface_management`).


```{figure} images/invesalius_screen/surface_config_panel_en.png
:name: 3d_surface_management
:align: center

3D surface
configuration.
```

### Creating 3D Surfaces

News surfaces can be created using an already segmented mask. To do so,
on the left panel under **3. Configure 3D surface**, click on the button
shown in {numref}`shortcut_new_surface`.

```{figure} images/icons/object_add_original.png
:name: shortcut_new_surface
:align: center

Button to create a 3D
surface.
```

After clicking this button, a dialog will be shown
({numref}`create_surface_1`). This dialog allows for the
configuration of the 3D surface created, including setting the quality
of the surface, filling surface holes whilst keeping the largest
connected region of the surface intact.

```{figure} images/invesalius_screen/surface_config_window_en.png
:name: create_surface_1
:align: center

3D surface creation
dialog.
```

The keep largest region option may be used, for instance, to remove the
tomograph supports. [Figures](#surface_model_front) display a surface created with **Keep
the largest region** and **Fill holes** activated, whereas
[Figures](#surface_model_front_all_parts) display the surface created without
activating that options. Note the tomograph support and the holes.

```{figure} images/invesalius_screen/surface_model_front.jpg
:name: surface_model_front
:align: center

Surface created with **Keep
the largest region** and **Fill holes** activated (front).
```

```{figure} images/invesalius_screen/surface_model_bottom.jpg
:name: surface_model_bottom
:align: center

Surface created with **Keep
the largest region** and **Fill holes** activated (bottom).
```

```{figure} images/invesalius_screen/surface_model_front_all_parts.jpg
:name: surface_model_front_all_parts
:align: center

Surface created without activating **Keep
the largest region** and **Fill holes** (front).
```

```{figure} images/invesalius_screen/surface_model_bottom_all_parts.jpg
:name: surface_model_bottom_all_parts
:align: center

Surface created without activating **Keep
the largest region** and **Fill holes** (bottom).
```


The **Surface creation method** item has the following options:
**Binary**, **Context aware smoothing** and **Default**.
[Figures](#binary) show an example of surface created using
each of these 3 methods.

The **Binary** method takes as input the segmentation mask which is
binary, where selected regions have value 1 and non-selected have value
*0*. As it is binary, the surface generated has a blocky aspect, mainly in
high-curvature areas, appearing staircases.

**Context aware smoothing** starts generating the surface using Binary,
then uses another algorithm in order to smooth the surface to avoid
staircase details. This method has 4 parameters presented below.

The **angle** parameter is the angle between 2 adjacent triangles. If
the calculated angle is greater than the angle parameter, the triangle
will be considered a staircase triangle and will be smoothed. The angle
parameter ranges from 0 to 1, where 0 is 0° and 1 is
90°. The **Max distance** is the maximum distance that a
non-staircase triangle may be from a staircase triangle to be considered
to be smoothed. Non-staircase triangles with distance greater than Max
distance also will be smoothed, but the smoothing will be determined by
the **Min. weight** parameter. This parameter ranges from 0 (without
smoothing) to 1 (total smoothing). The last parameter, **N.steps**, is
the number of times the smoothing algorithm will be run. The greater
this parameter the smoother the surface will be.

The **Default** method is enabled only when thresholding segmentation
was used without any manual modification to the mask. This method does
not use the mask image, but the raw image, and generates a smoother
surface.

```{figure} images/invesalius_screen/binary.png
:name: binary
:align: center

Surface generated with **Binary**.
```

```{figure} images/invesalius_screen/context.png
:name: context
:align: center

Surface generated with **Context aware smoothing**.
```

```{figure} images/invesalius_screen/default.png
:name: default
:align: center

Surface generated with **Default**.
```

### Transparency

The Transparency function allows for the displaying of a surface
transparently. To do so, select the desired surface from the list of
surfaces in the item **3. Configure 3D surface**, **Surface
properties** ({numref}`select_surface`).


```{figure} images/invesalius_screen/surface_select_menu_en.png
:name: select_surface
:align: center

Surface
selection.
```

Then, to set the level of surface transparency, use the sliding control
shown in {numref}`select_transparency`; the more to the right, the more
transparent the surface will be.


```{figure} images/invesalius_screen/surface_transparency_en.png
:name: select_transparency
:align: center

Selection of surface
transparency.
```

{numref}`model_transparency` shows 2 surfaces: the external
surface in green has some level of transparency which permits seeing the
internal surface in yellow.

```{figure} images/invesalius_screen/transparency_2.png
:name: model_transparency
:align: center

Surface with
transparency.
```

### Color

Surface colors can be altered by selecting the surface
({numref}`select_surface`), and clicking on the colored button on
the right of the surface selection list.
{numref}`change_surface_color` displays this button, inside item
**3. Configure 3D surface**, **Surface properties**.

```{figure} images/invesalius_screen/surface_button_select_color_yellow.png
:name: change_surface_color
:align: center

Button to change surface
color.
```

A dialog will be shown
({numref}`button_select_color`). Select the desired color and
click on **OK**.

```{figure} images/invesalius_screen/surface_select_color_windows_so_en.png
:name: button_select_color
:align: center

Color
dialog.
```

### Splitting Disconnected Surfaces

To split disconnected surfaces, select **3. Configure 3D surface**,
**Advanced options**
({numref}`advanced_tools`).

```{figure} images/invesalius_screen/surface_painel_advanced_options_en.png
:name: advanced_tools
:align: center

Advanced
options.
```

The advanced options panel will be displayed
({numref}`advanced_tools_expanded`).

```{figure} images/invesalius_screen/surface_split_en.png
:name: advanced_tools_expanded
:align: center

Advanced options
panel.
```

#### Select Largest Surface

The option **Select largest surface** selects, automatically, only
surface with the greater volume. Click on the button illustrated in
{numref}`short_connectivity_largest`. This operation creates new
a surface with only the largest surface.


```{figure} images/icons/connectivity_largest.png
:name: short_connectivity_largest
:align: center

Button to split the largest disconnected
surface.
```

As an example, the
{numref}`extract_most_region_1` shows a surface before **Select
the largest surface**.


```{figure} images/invesalius_screen/surface_extract_most_region_1.jpg
:name: extract_most_region_1
:align: center

Disconnected
surfaces.
```

Whereas the
{numref}`extract_most_region2` shows the surface with the largest
disconnected region separated.


```{figure} images/invesalius_screen/surface_extract_most_region2.jpg
:name: extract_most_region2
:align: center

Largest disconnected region
separated.
```

#### Select Regions of Interest

Another selection option is Select regions of interest. To do this
 operation, click on the button illustrated in
{numref}`short_connectivity_manual`, then click on the desired
disconnected surface regions you want to select. Next click on **Select
regions of interest**. This operation will create a new surface with
only the selected disconnected regions.

```{figure} images/icons/connectivity_manual.png
:name: short_connectivity_manual
:align: center

Button to select the regions of
interest.
```

As an example, the
{numref}`extract_most_region3` shows the surface created after
the user selects the cranium and the right part of the tomograph
support.

```{figure} images/invesalius_screen/surface_extract_most_region3.jpg
:name: extract_most_region3
:align: center

Example of selected regions of
interest.
```

#### Split All Disconnected Surfaces

Disconnected surface regions can also be split automatically. To do
this, click on the button illustrated in
{numref}`connectivity_split_all`.


```{figure} images/icons/connectivity_split_all.png
:name: connectivity_split_all
:align: center

Button to split all the disconnected regions
surface.
```

{numref}`extrac_most_region_4` shows an example.

```{figure} images/invesalius_screen/surface_extract_most_region_4.jpg
:name: extrac_most_region_4
:align: center

Example of split all disconnected regions
surface.
```

## Measures

InVesalius has linear and angular measurements in 2D (axial, coronal and
sagittal planes) and 3D (surfaces). It is thus possible to take
measurements of volume and area on surfaces.

### Linear Measurement

To perform linear measurements, activate the feature by clicking on the
shortcut shown below, located on the toolbar
({numref}`measure_line_original`).

```{figure} images/icons/measure_line_original.png
:name: measure_line_original
:align: center

Shortcut to activate linear
measurement.
```

A linear measurement is taken between two points. With the feature
enabled, click **once** on the image to set the starting point. Then
position the mouse pointer on the end point and click once again. The
measurement is performed and the result is automatically displayed on
the image or surface

{numref}`axial_linear` shows a 2D linear measure in the axial
orientation, and {numref}`3d_linear` shows another linear measure in 3D (surface).

Once you have made a 2D linear measurement, it can be edited by placing
the mouse on one end, holding down the **right mouse button** and
dragging it to the desired position.

```{figure} images/invesalius_screen/axial_linear.png
:name: axial_linear
:align: center

Linear measure on
image.
```

```{figure} images/invesalius_screen/3d_linear.jpg
:name: 3d_linear
:align: center

Linear measure on
surface.
```

**Note: The linear measurement is given in millimeters (mm).**

### Angular Measurement

An angular measurement in 2D on a surface (3D) can be done by clicking
on the shortcut shown in
{numref}`atalho_angular`.


```{figure} images/icons/measure_angle_original.jpg
:name: atalho_angular
:align: center

Shortcut for angle
measurement.
```

To perform the angular measurement, it is necessary to provide the three
points that will describe the angle to be measured, AB̂C. Insert the
first point by clicking once to select point A. Insert point B (the
vertex or \"point\" of the angle) by positioning the cursor and clicking
once again. Repeat the same actions to determine the endpoint of the
angle C. The resulting measurement is displayed on the image or
surface.

{numref}`axial_angular` illustrates an angular measurement on a
flat image; {numref}`axial_superficie` illustrates an angular measurement on
a surface.

In regard to 2D linear measurement, you can also edit the 2D angular
measurement. Just position the mouse on one end, hold down the right
mouse button and drag it to the desired position.


```{figure} images/invesalius_screen/axial_angular.png
:name: axial_angular
:align: center

Angular
measurement.
```

```{figure} images/invesalius_screen/angular_superficie.jpg
:name: axial_superficie
:align: center

Angular measurement on
surface.
```

**Note: Angular measurement is shown in degrees (°)**

### Volumetric Measurement

Volume and area measurements are made automatically when you create a
new surface. These are displayed in the **Surfaces 3D** tab in the
**Data** management panel, located in the bottom left corner of the
screen, as illustrated in
{numref}`volumetric_measure`.

```{figure} images/invesalius_screen/painel_volumetric_measures_en.png
:name: volumetric_measure
:align: center

Volumetric
measurements.
```

**Note: Volume measurement is given in cubic millimeter (mm<sup>3</sup>),
already the one of area in square millimeter (mm<sup>2</sup>).**

## Data Management

We have previously shown how to manipulate surfaces, masks for
segmentation and measurements. We can also show or hide and create or
remove these elements in the **Data** management panel, located in the
lower left corner of InVesalius. The panel is divided into 3 tabs:
**Masks**, **3D Surfaces** and **Measurements**, as shown in
{numref}`volumetric_data` Each tab contains features
corresponding to the elements it refers to.

```{figure} images/invesalius_screen/painel_mask_manager_en.png
:name: volumetric_data
:align: center

Data
management.
```

In each tab, there is a panel divided into rows and columns. The first
column of each line determines the visualization status of the listed
element. The \"eye\" icon activates or deactivates the masks, surface or
measurement displayed. When one of these elements is being displayed,
its corresponding icon (as shown in
{numref}`disable_mask`) will also be visible.


```{figure} images/invesalius_screen/eye.jpg
:name: disable_mask
:align: center

Icon indicating the elements
visibility.
```

Some operations may be performed with the data. For instance, to remove
one element, first select its name, as shown in
{numref}`selected_mask`. Next, click on the shortcut shown in
{numref}`delete_data`.


```{figure} images/invesalius_screen/painel_selected_mask_en.png
:name: selected_mask
:align: center

Data
selected.
```

```{figure} images/icons/data_remove.png
:name: delete_data
:align: center

Remove
data.
```

To create a new mask, surface or measurement, click on the shortcut
shown in {numref}`new_data`, provided that the corresponding tab is open.


```{figure} images/icons/data_new.png
:name: new_data
:align: center

New data.
```

To duplicate data, select data to be duplicated and click in the
shortcut shown in
{numref}`duplicate_data`.


```{figure} images/icons/data_duplicate.png
:name: duplicate_data
:align: center

Duplicate
data.
```

### Masks

In the Name column, the mask's color and name are shown. The
**Threshold** column shows the value range used to create the mask.
{numref}`volumetric_data` shows an example.

### 3D Surface

In the **Name** column, the surface's color and name are shown. The
**Volume** column shows the total surface volume. Finally, the
**Transparency** column indicates the level of transparency for use for
surface visualization.
{numref}`surface_manager` shows an example.

```{figure} images/invesalius_screen/painel_volumetric_measures_en.png
:name: surface_manager
:align: center

Surface
manager.
```

#### Import Surface

We can also import STL, OBJ, PLY or VTP (VTK Polydata File Format) files
into an active InVesalius project. To do so, click on the icon shown in
{numref}`import_stl`, select the format of the corresponding
file, ({numref}`import_surface`) and click Open.

```{figure} images/icons/load_mesh.png
:name: import_stl
:align: center

Shortcut to import surface.
```

```{figure} images/invesalius_screen/import_surface_en.png
:name: import_surface
:align: center

Window to import
surface.
```

### Measurements

The Measurements tab shows the following information. **Name** indicates
the color and measurement name. **Local** indicates where the
measurement was taken (image axial, coronal, sagittal or 3D), and
**Type** indicates the type of measurement (linear or angular). Finally,
**Value** shows the measurement value.
{numref}`manager_mensuares` illustrates the **Measurements** tab.

```{figure} images/invesalius_screen/painel_measures_manager_en.png
:name: manager_mensuares
:align: center

Data
management.
```

## Simultaneous Viewing of Images and Surfaces

Images and surfaces can be viewed simultaneously by **left-clicking** on
the shortcut
({numref}`slice_plane_original`) located in the lower right corner
of the InVesalius interface.

```{figure} images/icons/slice_plane_original.png
:name: slice_plane_original
:align: center

Shortcut for simultaneous
viewing.
```

This feature allows users to enable or disable the displaying of images
in different orientations (or plans) within the same display window of
the 3D surface. Simply check or uncheck the corresponding option in the
menu shown in {numref}`view_2d_3d_1`.

```{figure} images/invesalius_screen/view_2d_3d_1_en.png
:name: view_2d_3d_1
:align: center

Selection of the guidelines (plans) to
display.
```

It is worth noting that when a particular orientation is selected, a
check is presented in the corresponding option. This is illustrated in
{numref}`view_2d_3d_2`.


```{figure} images/invesalius_screen/view_2d_3d_2_en.png
:name: view_2d_3d_2
:align: center

Selected Guidelines for
display.
```

If the surface is already displayed, the plans of the guidelines will be
presented as shown in
{numref}`only_2d_planes`. Otherwise, only the plans will be
displayed.

```{figure} images/invesalius_screen/3d_planes.jpg
:name: 3d_planes
:align: center

Surface and plans displayed
simultaneously.
```

```{figure} images/invesalius_screen/only_2d_planes.jpg
:name: only_2d_planes
:align: center

Flat display (no
surface).
```

To view the display of a plan, just uncheck the corresponding option in
the menu ({numref}`view_2d_3d_2`).

(volume-rendering)=
## Volume Rendering

For volume rendering models, InVesalius employs a technique known as
raycasting. Raycasting is a technique that simulates the trace of a beam
of light toward the object through each screen pixel. The pixel color is
based on the color and transparency of each voxel intercepted by the
light beam.

InVesalius contains several pre-defined patterns (presets) to display
specific tissue types or different types of exam (tomographic contrast,
for example).

To access this feature, simply click the shortcut shown in
{numref}`volume_raycasting_origina` in the lower right corner of
the screen (next to the surface display window) and select one of the
available presets.

To turn off volume rendering, click again on the path indicated by
{numref}`volume_raycasting_origina` and select the **Disable**
option.


```{figure} images/icons/volume_raycasting_origina.png
:name: volume_raycasting_origina
:align: center

Shortcut to volume
visualization.
```

### Viewing Standards

There are several predefined viewing patterns. Some examples are
illustrated in the following figures.

```{figure} images/invesalius_screen/brilhante_I.jpg
:name: brilhante_I
:align: center

Bright.
```

```{figure} images/invesalius_screen/vias_aereas_II.jpg
:name: vias_aereas_II 
:align: center

Airway II.
```

```{figure} images/invesalius_screen/contraste_medio.jpg
:name: contraste_medio
:align: center

Contrast
Medium.
```

```{figure} images/invesalius_screen/MIP.jpg
:name: MIP
:align: center

MIP.
```

### Standard Customization

Some patterns can be personalized (and customized).
{numref}`customize_1` is exhibiting a pattern and some graphical
controls' adjustment. With these features, the color of a given structure
and its opacity can be altered, determining if and how it will be
displayed.

```{figure} images/invesalius_screen/customize_1.png
:name: customize_1
:align: center

Settings for the display pattern Soft Skin +
II.
```

To hide a structure, use the control setting chart to decrease the
opacity of the corresponding region. In the example in
{numref}`customize_1` suppose we want to hide the muscular part
(appearing in red). To do this, simply position the pointer over the
muscular part in red and, using the left mouse button, drag the point
down to reduce opacity and make the part transparent.
{numref}`customize_2` illustrates the result.

Note: The Alpha value indicates the opacity of the color and the
**value**, the color intensity of the pixel.

```{figure} images/invesalius_screen/customize_2.png
:name: customize_2
:align: center

Display Standard Soft Skin + II
changed.
```

We can also remove or add points on the graph control setting. To
remove, simply click with the right mouse button on the point. To add a
new point, click the left button on the line graph. One can also save
the resulting pattern by clicking the shortcut shown in
{numref}`save_preset`.

```{figure} images/invesalius_screen/save_preset.png
:name: save_preset
:align: center

Shortcut to save
standard.
```

To save the pattern, InVesalius displays a window like the one shown in
{numref}`save_window_preset`. Enter a name for the custom pattern
and **click OK**. The saved pattern will be available for the next time
the software is opened.

```{figure} images/invesalius_screen/save_window_preset_en.png
:name: save_window_preset
:align: center

Window to save name of
pattern.
```

### Standard Customization with Brightness and Contrast

You can customize a pattern without using the graphical control settings
presented in the previous section. This is done through the **brightness
and contrast** controls on the toolbar. Activate these by clicking the
icon shown in
{numref}`tool_contrast_original_vol`.


```{figure} images/icons/tool_contrast_original.png
:name: tool_contrast_original_vol
:align: center

Shortcut to Brightness and
Contrast.
```

Enable the control by dragging the mouse, with the left button pressed
on the volume window. This will change the values of the window width
and window level. The procedure is the same as with slices applied to 2D
images, which can be seen in
[Brightness and contrast](#brightness-and-contrast-windows).
Dragging the mouse in a horizontal direction changes the window level
value; drag left to decrease and right to increase. Dragging the mouse
vertically changes the value of window width; drag down to decrease and
up to increase.

Manipulating these values can be useful for different viewing results.
For example, to add tissue to the display, **drag** the mouse diagonally
with **left button** pressed from the lower right to the upper left
corner of the preview window. To remove tissue visualization, do the
opposite, (i.e., drag the mouse diagonally from top left to bottom right
with the left button pressed). See
{numref}`raycasting_add_2`.

```{figure} images/invesalius_screen/raycasting_add_2.PNG
:name: raycasting_add_2
:align: center

Raycasting.
```

### Cut

In volume rendering, the cut function is used to view a cross-section of
a region. With a volume pattern selected, click **Tools**, and then
click **Cut plane**
({numref}`activate_cut_plane`).


```{figure} images/invesalius_screen/activate_cut_plane_en.png
:name: activate_cut_plane
:align: center

Enabling plan to
cut.
```

An outline for cutting appears next to the volume. To make the cut, hold
the left mouse button on the plane and drag the mouse. To rotate the
plane, hold the left mouse button pressed on its edge and move the mouse
in the desired direction as shown in
{numref}`cutted_image`.


```{figure} images/invesalius_screen/cutted_image.png
:name: cutted_image
:align: center

Image with clipping
plane.
```

When finished using the function, click **Tools** and again click **Cut
plane** ({numref}`cutted_image`).

## Stereoscopic Visualization

InVesalius supports stereoscopic visualization of 3D models. First, a
surface (see [Surfaces](#surface-triangle-mesh)) or an active volumetric visualization (see
[Volume rendering](#volume-rendering)) must be created. Then, click the icon (shown
in {numref}`ster`) on the bottom right part of the interface and choose the desired
projection type ({numref}`st_menu`).

```{figure} images/icons/3D_glasses.png
:name: ster
:align: center

Shortcut to activate stereoscopic viewing
methods.
```


```{figure} images/invesalius_screen/st_menu_en.png
:name: st_menu
:align: center

Different methods of stereoscopic
visualization.
```

InVesalius supports the following types of stereoscopic viewing:

-   Red-blue

-   Anaglyph

-   CristalEyes

-   Interlaced

-   Left

-   Right

-   Dresden

-   Checkboard

[Figures](#st_surf_red_blue) below present three different types of
projections.

```{figure} images/invesalius_screen/st_surf_red_blue.jpg
:name: st_surf_red_blue
:align: center

Red-blue projection.
```

```{figure} images/invesalius_screen/st_surf_anaglyph.jpg
:name: st_surf_anaglyph
:align: center

Anaglyph projection.
```

```{figure} images/invesalius_screen/st_surf_interlaced.jpg
:name: st_surf_interlaced
:align: center

Interlaced projection.
```

## Data Export

InVesalius can export data in different formats, such as OBJ, STL and
others, to be used in other software.

The menu to export data is located in the left panel of InVesalius,
inside item **4. Export data** (displayed below in
{numref}`data_export`). If the menu is not visible, double-click
with the **left** mouse button to expand the item.

```{figure} images/invesalius_screen/painel_data_export_en.png
:name: data_export
:align: center

Menu to export
data.
```

### Surface

To export a surface, select it from the data menu as shown in
{numref}`data_export_selection`.

```{figure} images/invesalius_screen/painel_data_export_selection_en.png
:name: data_export_selection
:align: center

Select surface to be
exported.
```

Next, click on the icon shown in
{numref}`surface_export_original`.

```{figure} images/icons/surface_export_original.png
:name: surface_export_original
:align: center

Shortcut to export
surface.
```

When the file window displays (as shown in
{numref}`export_data_window`), type the file name and select the
desired exported format. Finally, click **Save**.

```{figure} images/invesalius_screen/export_surface_en.png
:name: export_data_window
:align: center

Window to export
surface.
```

Files formats available for exportation in InVesalius are listed in the table below.

****

(files-export-list)=
| Format                     | Extension |
|----------------------------|-----------|
| Inventor                   | .iv       |
| Polygon File Format        | .ply      |
| Renderman                  | .rib      |
| Stereolithography (binary) | .stl      |
| Stereolithography (ASCII)  | .stl      |
| VRML                       | .vrml     |
| VTK PolyData               | .vtp      |
| Wavefront                  | .obj      |


### Image

Images exhibited in any orientation (axial, coronal, sagittal and 3D)
can be exported. To do so, **left-click** on the shortcut shown in
{numref}`menu_save_image_window` and select the sub-window
related to the target image to be exported.


```{figure} images/invesalius_screen/menu_save_image_window_en.png
:name: menu_save_image_window
:align: center

Menu to export
images.
```

On the window shown
({numref}`save_image_window`), select the desired file format,
then click **Save**.


```{figure} images/invesalius_screen/export_bmp_en.png
:name: save_image_window
:align: center

Window to export
images.
```

## Customization

Some customization options are available for InVesalius users. They are
shown as follows.

### Tools Menu

To hide/show the side tools menu, click the button shown in
{numref}`layout_full_original`.

```{figure} images/icons/layout_full_original.png
:name: layout_full_original
:align: center

Shortcut to hide/show side tools
menu.
```

With the menu hidden, the image visualization area in InVesalius is
expanded, as shown in
{numref}`closed_tool_menu`.

```{figure} images/invesalius_screen/window_mpr_not_painels_en.png
:name: closed_tool_menu
:align: center

Side menu
hidden.
```

### Automatic Positioning of Volume/Surface

To automatically set the visualization position of a volume or surface,
click on the icon shown in
{numref}`3d_automatic_position` (located in the inferior right
corner of InVesalius screen) and choose one of the available options for
visualization.

```{figure} images/invesalius_screen/3d_automatic_position_en.png
:name: 3d_automatic_position
:align: center

Options for visualization
positioning.
```

### Background Color of Volume/Surface Window

To change the background color of the volume/surface window, click on
the shortcut shown in
{numref}`button_select_color_2`. The shortcut is also located in
the lower right corner of the InVesalius screen.

```{figure} images/invesalius_screen/colour_button_en.png
:name: button_select_color_2
:align: center

Shortcut to background color of volume/surface
window.
```

A window for color selection opens
({numref}`color_window_background`). Next, simply click over the
desired color and then click **OK**.


```{figure} images/invesalius_screen/surface_select_color_windows_so_en.png
:name: color_window_background
:align: center

Background color
selection.
```

{numref}`background_color` illustrates an InVesalius window with
the background color changed.


```{figure} images/invesalius_screen/3d_background_changed.png
:name: background_color
:align: center

Background color
modified.
```

### Show/Hide Text in 2D Windows

To show or hide text in 2D image windows, click on the shortcut
illustrated in {numref}`text` on the toolbar.


```{figure} images/icons/text.png
:name: text
:align: center

Shorcut to show or hide
texts.
```

{numref}`text_on` and {numref}`text_off` show text enabled and disabled, respectively.


```{figure} images/invesalius_screen/axial_en.png
:name: text_on
:align: center

Show texts
enabled.
```

```{figure} images/invesalius_screen/axial_no_tex_en.png
:name: text_off
:align: center

Show texts
disabled.
```

## Neuronavigation

Neuronavigation is a technique that allows tracking and localization of
surgical instruments relative to neuronal structures through computer
visualization. In addition, neuronavigation systems are a fundamental tool
to aid surgical plan and to increase the accuracy of experiments in
neuroscience, such as transcranial magnetic stimulation (TMS),
electroencephalography (EEG), magnetoencephalography (MEG) and
near-infrared spectroscopy (NIRS). Despite the vast field of
applications, the use of neuronavigation in research centers is limited
by its high cost. InVesalius Navigator offers users a low-cost,
open-source alternative to commercial neuronavigation systems. In this
sense, it is possible to use specific tools for neuronavigation and
still have the possibility of developing features on demand. The
software for neuronavigation is distributed in an executable version compatible with Windows 7, 8 and 10 operating system. 

The following sections explain different steps of neuronavigation such as setting up the tracker, creating and editing markers, 
brain segmentation and creating 3D surface of the head.

### Setting up the tracking device

**1.** Open Preferences ({numref}`preferences`).

```{figure} images/invesalius_screen/preferences.png
:name: preferences
:align: center

Preferences
```

**2.** Go to the tracker tab and choose the tracking device from the dropdown menu as seen in {numref}`select_tracker`.

```{figure} images/invesalius_screen/select_tracker_optitrack.png
:name: select_tracker
:align: center

Tracker selection
```
#### Optitrack

When using Optitrack, select the Motive calibration file and user profile file for that tracker ({numref}`configure_optitrack`) 
and click **OK** and **OK** again.

```{figure} images/invesalius_screen/configure_optitrack.png
:name: configure_optitrack
:align: center

Configure Optitrack
```

#### Polaris

Configuring Polaris requires choosing the COM port or IP, and ROM files ({numref}`configure_polaris`)

**COM port or IP**: Choose the connection to the camera. Typical COM ports are:
- Windows: COM1
- Linux: /dev/ttyUSB0
- Mac: /dev/tty.usbserial-001014FA

**ROM files**: Each passive marker tool has its own ROM file that defines its geometry for Polaris. 
    For example, if you are using the Magstim NT-115 as the probe, select NT-115.rom as Probe ROM file. 

```{figure} images/invesalius_screen/configure_polaris.png
:name: configure_polaris
:align: center

Configure Polaris
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/connecting_to_cameras.mp4", width="640" height="360"/>
```

### Stimulator configuration

**1.** Open Preferences ({numref}`preferences2`) and go to the stimulator tab.

```{figure} images/invesalius_screen/preferences.png
:name: preferences2
:align: center

Preferences
```

**2.** You can create a new stimulator registration or load an existing registration 
from OBR file as seen in {numref}`stimulator_config`.

```{figure} images/invesalius_screen/stimulator_configuration.png
:name: stimulator_config
:align: center

Loading stimulator registration from a file
```

**3.** Here you can also change the angle threshold, distance threshold, 
and timestamp interval of the stimulator ({numref}`preferences_stimulator`)

```{figure} images/invesalius_screen/preferences_stimulator.png
:name: preferences_stimulator
:align: center

Stimulator configuration
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/stimulator_configuration.mp4", width="640" height="360"/>
```

### Creating head surface

**1.** Go to **Imports section** → **1. Load data** and select either **Import DICOM images** or **Import NIFTI images** 
and select the file to load ({numref}`import_nifti`). For MRI images NIFTI is the preferred file type 
because it enables automatic brightness adjustment.

```{figure} images/invesalius_screen/import_nifti_image.png
:name: import_nifti
:align: center

Import NIFTI image
```

**2.** Go to **Imports section** → **2. Select region of interest** and set the minimum and maximum threshold 
by moving the two sliders on the bar. The threshold should be set so that only the head is colored 
in the slice windows as seen in {numref}`correct_threshold` below.

```{figure} images/invesalius_screen/correct_threshold.png
:name: correct_threshold
:align: center

Correctly set threshold
```

{numref}`incorrect_threshold` shows an example of **incorrectly** set threshold for the mask. 
There should not be any dots visible outside of the head in the mask. 

```{figure} images/invesalius_screen/incorrect_threshold.png
:name: incorrect_threshold
:align: center

Incorrectly set threshold
```

**3.** Once the mask threshold is set, click **Create surface** button 
to create a 3D surface of the head ({numref}`head_with_artefacts`).

```{figure} images/invesalius_screen/3d_head_with_artefacts.png
:name: head_with_artefacts
:align: center

3D surface of the head
```

**4.** Go to the **Imports section** → **3. Configure 3D surface** → **Advanced options** and click **Select largest surface** 
to remove small disconnected parts of the surface. The disconnected parts can be clearly seen in the 3D view in the previous image. 
This process creates a new surface in the **Data** section, where the disconnected parts have been removed as seen in {numref}`head_without_artefacts`.

```{figure} images/invesalius_screen/3d_head_without_artefacts.png
:name: head_without_artefacts
:align: center

Cleaned up 3D surface of the head
```

**5.** To refine the surface further, select **Plugins** → **Remove non-visible faces** ({numref}`non_visible_faces`). 
Removing non-visible faces is also required to perform the “Refine” step at the end of coregistration. 

```{figure} images/invesalius_screen/remove_non_visible_faces.png
:name: non_visible_faces
:align: center

Remove non-visible faces
```

**6.** From the dropdown menu select the desired surface ({numref}`non_visible_faces_surface`), which in this case is usually the newest surface, 
and click **Apply**. This also creates a new surface in the **Data** section.

```{figure} images/invesalius_screen/remove_non_visible_faces_surface.png
:name: non_visible_faces_surface
:align: center

Select which surface to remove non-visible faces from
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/creating_head_surface.mp4", width="640" height="360"/>
```

### Renaming surfaces

Go to the **Data** section at the bottom left corner, open the 3D surfaces tab, 
and double click the name of the surface you want to change and type a new name ({numref}`rename_surface`).

```{figure} images/invesalius_screen/rename_surface.png
:name: rename_surface
:align: center

Rename surface
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/naming_surfaces.mp4", width="640" height="360"/>
```

### Recoloring surfaces

**1.** Go to **Imports section** → **3. Configure 3D surface** → **Surface properties**

**2.** Select the surface from the dropdown menu and click the colored square 
next to it to change the color as shown in {numref}`recolor_surface`. 
You can also change the transparency of the surface with the transparency slider.

```{figure} images/invesalius_screen/recolor_surface.png
:name: recolor_surface
:align: center

Recolor surface
```

It is also possible to edit the color right-clicking the surface in the **Data** → **3D surfaces** 
and selecting **Change color** ({numref}`recolor_surface_menu`).

```{figure} images/invesalius_screen/recolor_surface_context_menu.png
:name: recolor_surface_menu
:align: center

Recolor surface via context menu
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/coloring_surfaces.mp4", width="640" height="360"/>
```

### Brain segmentation

**1.** Go to **Tools** → **Segmentation** → **Brain segmentation MRI T1** ({numref}`brain_segmentation`)

```{figure} images/invesalius_screen/brain_segmentation.png
:name: brain_segmentation
:align: center

Brain segmentation
```

**2.** Select the backend and device, use Pytorch backend when using the CPU, 
and click **Segment** ({numref}`brain_segmentation_backend`). Depending on the computer, this can take several minutes.

```{figure} images/invesalius_screen/brain_segmentation_backend.png
:name: brain_segmentation_backend
:align: center

Brain segmentation configuration
```

**3.** After segmentation, go to **Imports section** → **2. Select region of interest** 
and click **Create surface** ({numref}`create_brain_surface`).

```{figure} images/invesalius_screen/create_surface.png
:name: create_brain_surface
:align: center

Create a brain surface
```

**4.** As seen in {numref}`brain_surface`, this creates a 3D surface of the brain, 
which visibility and color can be changed in the **Data** section on the **3D surfaces** tab.

```{figure} images/invesalius_screen/surfaces.png
:name: brain_surface
:align: center

Brain surface
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/brain_segmentation.mp4", width="640" height="360"/>
```

### Peeling the brain

**1.** Once the brain has been segmented, it is possible to create a peel 
by going to **Imports section** → **5. Tractography** and clicking **Peel** ({numref}`peeling_brain`).

```{figure} images/invesalius_screen/peeling_the_brain.png
:name: peeling_brain
:align: center

Peeling the brain
```

**2.** Select the brain segmentation mask and click **OK** ({numref}`create_peel`)). 
You can also import a mask file from another program such as Freesurfer or FSL in NIfTI format.

```{figure} images/invesalius_screen/create_peel.png
:name: create_peel
:align: center

Create peel
```

**3.** The peeled brain will appear in the volume window and parameters 
such as peeling depth can be edited in the tractography panel as seen in {numref}`peeled_brain`.

```{figure} images/invesalius_screen/peeled_brain.png
:name: peeled_brain
:align: center

Peeled brain
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/peeled_brain.mp4", width="640" height="360"/>
```

### Registering image fiducials

**1.** Go to **Navigation section** → **Coregistration** → **Image**

**2.** Click **Start registration** and place the cross tool in the slice windows on one of the three fiducials; 
left ear, right ear, and nasion. Once the cross tool is on the fiducial point, 
record that fiducial by clicking the corresponding fiducial button. 

Keep in mind that the right ear is on the left side and the left ear on the right side in the slice windows 
as indicated by the letters "R" and "L" which can be seen at the edges of each slice window in {numref}`image_fiducials`.

```{figure} images/invesalius_screen/image_fiducials.png
:name: image_fiducials
:align: center

Registering image fiducials
```

**3.** Repeat this process to register the rest of the image fiducials.

**Example video:**

```{raw} html
<video controls src="../_static/videos/image_fiducials.mp4", width="640" height="360"/>
```

### Registering tracker fiducials

**1.** Go to **Navigation section** → **Coregistration** → **Tracker**

**2.** Make sure that the tracker is configured and show as current tracker 
({numref}`tracker_fiducials`), and if not, click **Change tracker** to configure it.

```{figure} images/invesalius_screen/register_tracker_fiducials.png
:name: tracker_fiducials
:align: center

Tracker tab
```

**3.** The fiducials are color-coded; red indicates that the fiducial has not been recorded, 
green indicates that the fiducial has been recorded, 
and yellow indicates the currently selected fiducial that should be recorded next.

**4.** Click **Start registration** and record the fiducial that is shown in yellow 
by placing the tip of the marker probe to the fiducial point on the subject’s head, 
and either clicking the **Record fiducial** button or pressing the pedal if it is connected ({numref}`record_tracker_fiducials`).

```{figure} images/invesalius_screen/tracker_fiducials_color_coded.png
:name: record_tracker_fiducials
:align: center

Recording tracker fiducials
```

**5.** Continue this process for the other two fiducials, always recording the fiducial highlighted in yellow next.

**6.** Once all the fiducials have been recorded, make sure that you applied removed non-visible faces in **Plugins** → **Remove non-visible faces** 
and then click **Next** to move to the Refine tab and if the fiducial registration error (FRE) is too high, click **Refine** ({numref}`refine_coregistration`).

```{figure} images/invesalius_screen/refine_coregistration.png
:name: refine_coregistration
:align: center

Refine coregistration
```

**7.** When refining the registration, register at least 5 additional points on the subject’s head
 by placing the tip of the marker probe on the head and clicking Create point as shown in {numref}`refine_coregistration_ui`.

```{figure} images/invesalius_screen/refine_coregistration_ui.png
:name: refine_coregistration_ui
:align: center

Refine coregistration window
```

**8.** Once refining is done, click **Apply registration** and **Done**.

**Example video:**

```{raw} html
<video controls src="../_static/videos/tracker_fiducials.mp4", width="640" height="360"/>
```

### Creating markers

Go to **Navigation section** → **Navigation** and now you can use the cross tool ({numref}`cross_tool`)
 to select a location where you would like to create a marker. 

```{figure} images/invesalius_screen/cross_tool.png
:name: cross_tool
:align: center

Cross tool
```

Then click the **Create marker** button and a new landmark-type marker is created at that location as shown in {numref}`create_marker`. 
If you do not select a location using the cross tool, clicking **Create marker** will create 
a new marker at the center of the stimulator coil by default. 

```{figure} images/invesalius_screen/create_marker.png
:name: create_marker
:align: center

Create marker
```

When the stimulator is used to give TMS pulses, if the USB-TTL cable is connected, each pulse creates a marker 
at the center of the stimulator. In this case the type of the created markers is coil target, 
which means they can be directly set as targets by right-clicking the marker and selecting **Set as target**.

This is different from landmark-type markers, which must be first made into coil targets by right-clicking 
the marker and selecting **Create coil target** and then the new coil target marker 
can be directly set as target the same way as markers created from TMS pulses. 

**Example video:**

```{raw} html
<video controls src="../_static/videos/creating_markers.mp4", width="640" height="360"/>
```

### Editing markers

**1.** Go to **Navigation section** → **Navigation** and right click on a marker in the list to open a context menu 
with options to edit the label and color of the marker, and depending on the marker type, 
also create a coil or brain target, or set the marker as target ({numref}`editing_markers`).

```{figure} images/invesalius_screen/editing_markers.png
:name: editing_markers
:align: center

Editing markers
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/editing_markers.mp4", width="640" height="360"/>
```

### Robot target positioning

Once the fiducials have been recorded, tracker and stimulator have been configured, and the robot is connected, 
you can create targets and have the robot move the stimulator to the target. Go to **Navigation section** → **Navigation**, 
set a marker as a target by right-clicking it and selecting set as target, and click **Start neuronavigation** and make sure the 
"Track target with robot" button with the crane icon is enabled at the bottom left corner of the navigation buttons ({numref}`robot_targeting`). 
This will automatically start moving the stimulator to the target.

```{figure} images/invesalius_screen/robot_targeting.png
:name: robot_targeting
:align: center

Robot target positioning
```

**Example video:**

```{raw} html
<video controls src="../_static/videos/robot_target_positioning.mp4", width="640" height="360"/>
```

### Manual target positioning

**1.** For manual coil positioning, there is a target mode, which can be activated by going to **Navigation section** → **Navigation**, 
setting a target and clicking the **Start neuronavigation** button, and clicking the **Target mode** button under the marker list ({numref}`manual_targeting`).

```{figure} images/invesalius_screen/manual_target_positioning.png
:name: manual_targeting
:align: center

Manual target positioning
```

**2.** In target mode in the volume viewer, there are three images of the coil representing the orientation of the coil regarding the yaw, pitch, and roll rotations. 
There are also visible arrows that help guide the coil in correct orientation along those three axes. The goal is to move the coil and reduce the size of the arrows 
until the arrows disappear and each of the three small coils turns green. This means that the orientation of the coil is correct along all 
the corresponding axes. When adjusting the coil orientation, it is usually easier to focus on one axis at a time instead of all at once.

The volume window also displays the distance from the center of the coil to the target to help get close to the target without accidentally hitting the subject's head.

**Example video:**

```{raw} html
<video controls src="../_static/videos/manual_target_positioning.mp4", width="640" height="360"/>
```
