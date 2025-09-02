import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/widgets/donthave%20Account.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';

import '../widgets/authtxtOfTextField.dart';
import '../widgets/subheadtxt.dart';
import '../widgets/txtfield.dart';

class Signup extends StatelessWidget {
  const Signup({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: Text('sign In',
          style: TextStyle(
              color:Colors.black,
              fontWeight: FontWeight.bold
          ),
        ),
        centerTitle: true,
        leading: BackButton(),
      ),

      body: SingleChildScrollView(
        child: Padding(padding: const EdgeInsets.symmetric(horizontal: 16),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [

              const Subheadtxt(txt: 'Join us to build better habits for body and mind.'),
              SizedBox(height: 20,),
              const Authtxtoftextfield(txt: '  Name',),
              SizedBox(height: 5,),
              const CustomTextField(labelText: 'Enter your name', icona: Icons.person,),
              SizedBox(height: 16,),
              const Authtxtoftextfield(txt: '  Email',),
              SizedBox(height: 5,),
              const CustomTextField(labelText: 'Enter Email', icona: Icons.email,),
              SizedBox(height: 16,),
              const Authtxtoftextfield(txt: '  password',),
              SizedBox(height: 5,),
              const CustomTextField(labelText: 'Enter password', icona: Icons.password,),
              SizedBox(height: 16,),
              const Authtxtoftextfield(txt: '  Confirm password',),
              SizedBox(height: 5,),
              const CustomTextField(labelText: 'Enter your password again', icona: Icons.password,),
              SizedBox(height: 40,),
              Mainbutton(func: (){}, txt: 'Sign Up'),
              DontHaveAccount(buttontext: 'Already have account ?', normaltext: 'Sign In', func: () {  },),
              SizedBox(height: 12,),
              Image.asset('assets/or.png'),
              SizedBox(height: 12,),
              Image.asset('assets/google.png'),

            ],
          ),
        ),
      ),
    );
  }
}




