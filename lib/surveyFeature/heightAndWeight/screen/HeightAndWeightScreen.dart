import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';

import '../../../auth/view/widgets/authtxtOfTextField.dart';
import '../../../auth/view/widgets/txtfield.dart';
import '../../genderAndStatus/screen/genderAndStatusScreen.dart';
import '../../widgets/numofsurvey.dart';

class Heightandweightscreen extends StatelessWidget {
  const Heightandweightscreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading:const  BackButton(),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              const SizedBox(height: 36,),
              Image.asset('assets/survey2.png'),
              const SizedBox(height: 7,),
              const NumOfSurvey(num: '4/15',),
              const SizedBox(height: 80,),
              const Authtxtoftextfield(txt: ' Height',),
              const SizedBox(height: 8,),
              const CustomTextField(labelText: 'Enter your Height', icona: Icons.accessibility_new,),
              const SizedBox(height: 32,),
              const Authtxtoftextfield(txt: 'Weight',),
              const SizedBox(height: 8,),
              const CustomTextField(labelText: 'Enter your Weight', icona: Icons.monitor_weight,),
              const SizedBox(height: 120,),
              Mainbutton(func: (){
                Navigator.push(context, MaterialPageRoute(builder: (context)=>const Genderandstatusscreen()));
              }, txt: 'Next'),
            ],
          ),
        ),
      ),
    );
  }
}
