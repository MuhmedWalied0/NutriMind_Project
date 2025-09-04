import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';
import 'package:tester/surveyFeature/name/screen/nameScreen.dart';

class Startsurveyscreen extends StatelessWidget {
  const Startsurveyscreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body:Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          const SizedBox(height: 133,),
          Image.asset('assets/board.png'),
          const SizedBox(height: 56,),
         const Text('Your Health Survey',
          style: TextStyle(
            color: Colors.black,
            fontWeight: FontWeight.bold,
            fontSize: 20
          ),
          ),
          const SizedBox(height: 16,),
          const Text('Help us to understand your health and \n   daily habbits so we can create \na personlaized nutrition plan for you',
          ),
          const SizedBox(height: 110,),
          Mainbutton(func: (){
            Navigator.push(context, MaterialPageRoute(builder: (context)=>const Namescreen()));
          }, txt: 'Start Now'),
        ],
      ),
    );
  }
}











