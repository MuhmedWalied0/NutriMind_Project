import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class DontHaveAccount extends StatelessWidget {
  const DontHaveAccount({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text('Don’t have account ? ',
          style: TextStyle(
            color:Colors.black,
          ),
          ),
          TextButton(onPressed: (){},
              child: const Text('Sign Up',
              style: TextStyle(
                color: Color(0xff207344),
              ),
              ))
        ],
    );
  }
}
