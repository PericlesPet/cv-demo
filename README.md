# Καλωσήρθατε στο demo μηχανικής μάθησης της Aristurtle

Έχουμε φροντίσει ώστε ότι είναι να τρέξει είναι έτοιμο σε bash script στην ρίζα του φακέλου cv-demo.

Υπάρχουν λοιπόν 4 bash scripts, τα run_darknet.sh,  run_yolomark.sh, run_label_conversion_pt1.sh, run_label_conversion_pt2.sh και run_BEV.sh, τα οποία εξηγούνται παρακάτω.  

## Darknet
Στον φάκελο “darknet“ υπάρχει ένα fork του darknet με το δικό μας σετ εκπαίδευσης και μερικές εικόνες για επαλήθευση. Υπάρχουν επίσης όλα τα προσαρμοσμένα αρχεία .cfg, καθώς και κάποια ακόμα αρχεία που έπρεπε να αλλάξουμε για να κάνουμε εκπαίδευση στα δικά μας δεδομένα. 
Λόγω του περιορισμού μεγέθους του github όμως, στο demo/darknet υπάρχει μόνο η αρχιτεκτονική YOLOv3 Tiny ενδεικτικά, αφού τα βάρη των άλλων 2 μοντέλων είναι περίπου 250MB το καθένα. Επίσης υπάρχουν μόνο λίγες από τις εικόνες για επαλήθευση, καθώς το αρχικό σετ για επαλήθευση είναι περίπου 1GB και το σετ εκπαίδευσης είναι 15GB.

Παρόλαυτα, τα βάρη του YOLOv3 Tiny είναι εκπαιδευμένα στο κανονικό, ολόκληρο σετ εκπαίδευσης, οπότε τα αποτελέσματα που θα δείτε στο σετ επαλήθευσης είναι αντιπροσωπευτικά.

Παράλληλα, υπάρχει και ένα .pdf έγγραφο που γράψαμε ως εγχειρίδιο χρήσης του darknet, από το οποίο αφαιρέσαμε ότι δεν χρειαζόταν, για τα διάφορα προγράμματα και βιβλιοθήκες που χρειάζονται για να τρέξει το νευρωνικό.

Birds Eye View (BEV)
Στον φάκελο BEV υπάρχει επίσης ένα παράδειγμα σε python του μετασχηματισμού Bird’s Eye View. 
Χρειάζεται εγκατάσταση του OpenCV για Python.



Label Conversion
Στον φάκελο label conversion έχουμε ένα παράδειγμα από την μετατροπή των “label” των σετ δεδομένων των άλλων ομαδών στα δικά μας μέτρα. Στην πραγματικότητα χρησιμοποιήθηκαν πολλά script για conversion από διάφορα format, όπως VOC, XML based, MIT LabelMe Webtool format , και διάφορα άλλα. Στην προκειμένη περίπτωση το παράδειγμα είναι απλά για την αλλαγή των δεικτών των κλάσεων σε ενα ολόκληρο “dataset” όταν είναι και αυτό σε Yolo Darknet Format, αλλά με διαφορετική δεικτοδότηση. Κάθε dataset χρειάζεται ξεχωριστή αντιμετώπιση συνήθως και αρκετές φορές χρειαζόταν να αλλάζουν λεπτομέρειες στον κώδικα python ώστε να καλυφθούν κάποιες επιπλέον ιδιοτροπίες.
Επίσης πρέπει να σημειωθεί ότι το κομμάτι της τακτοποίησης και διαμόρφωσης του dataset στα μέτρα μας ήταν από τα πιο χρονοβόρα (από άποψη εργατοωρών) κομμάτια, καθώς υπάρχουν περίπου 35~ σετ δεδομένων από διαφορετικές ομάδες και για καθεμία χρειαζόταν δουλειά, κάποιες περισσότερο από άλλες.



### Parameters 

In IPMapping.py,
Toggle the parameter {plot} to 1 for visualization of whats going on

In generateMap.py,

#### Image Specs 
IMAGE_H
IMAGE_W
WARPED_IMG_H
WARPED_IMG_W
img_path

#### Focal Lengths
Fx
Fy

#### Cone Specs
coneRadius
xDisp
yDisp

### Running

```
python IPMapping.py
```

