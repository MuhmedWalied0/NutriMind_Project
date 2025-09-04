import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';

import '../../../auth/view/widgets/authtxtOfTextField.dart';
import '../../../auth/view/widgets/txtfield.dart';
import '../../heightAndWeight/screen/HeightAndWeightScreen.dart';
import '../../widgets/numofsurvey.dart';

class Namescreen extends StatelessWidget {
  const Namescreen({super.key});

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
              Image.asset('assets/survey1.png'),
              const SizedBox(height: 7,),
              const NumOfSurvey(num: '2/15',),
              const SizedBox(height: 80,),
              const Authtxtoftextfield(txt: 'First  Name',),
              const SizedBox(height: 8,),
              const CustomTextField(labelText: 'Enter your first name', icona: Icons.person,),
              const SizedBox(height: 32,),
              const Authtxtoftextfield(txt: 'last  Name',),
              const SizedBox(height: 8,),
              const CustomTextField(labelText: 'Enter your first name', icona: Icons.person,),
              const SizedBox(height: 120,),
              Mainbutton(func: (){
                Navigator.push(context, MaterialPageRoute(builder: (context)=>const Heightandweightscreen()));
              }, txt: 'Next'),
            ],
          ),
        ),
      ),
    );
  }
}
