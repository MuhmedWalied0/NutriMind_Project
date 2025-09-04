import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';

import '../../../auth/view/widgets/authtxtOfTextField.dart';
import '../../widgets/choosedContainer.dart';
import '../../widgets/numofsurvey.dart';

class Genderandstatusscreen extends StatelessWidget {
  const Genderandstatusscreen({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        leading:const BackButton(),
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 16.0),
        child: Column(
          //mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const SizedBox(height: 36,),
            Image.asset('assets/survey3.png'),
            const SizedBox(height: 7,),
            const NumOfSurvey(num: '6/15',),
            const SizedBox(height: 80,),
            const Authtxtoftextfield(txt: ' Gender',),
            const SizedBox(height: 12,),
            const Center(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Choosedcontainer(txt: 'Male',),
                    SizedBox(width: 40,),
                    Choosedcontainer(txt: 'Female',),
                  ]
              ),
            ),
            const SizedBox(height: 62,),
            const Authtxtoftextfield(txt: ' Status',),
            const Center(
              child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Choosedcontainer(txt: 'Student',),
                    SizedBox(width: 40,),
                    Choosedcontainer(txt: 'Employee',),
                  ]
              ),
            ),
           const  SizedBox(height: 112,),
            Mainbutton(func: (){}, txt: 'Next')
        ],
        ),
      ),
    );
  }
}




