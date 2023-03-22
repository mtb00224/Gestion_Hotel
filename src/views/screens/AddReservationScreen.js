import React, { useState } from 'react-native';
import { View, Text, TextInput, StyleSheet, Button, SafeAreaView ,TouchableOpacity} from 'react-native';
import COLORS from '../../consts/colors';
import Icon from 'react-native-vector-icons/MaterialIcons';

const AddReservationScreen = () => {


  return (
    <SafeAreaView>
            <View style={styles.header}>
                <View style={{paddingBottom: 15}}>
                    <Text style={{fontSize: 30, fontWeight: 'bold', color: COLORS.primary}}>
                        Hotel Gazelle
                    </Text>
                </View>
                <Icon name="person-outline" size={38} color={COLORS.grey} />
            </View>
            
            <View style={styles.container}>
      <Text style={styles.label}>First Name</Text>
      <TextInput
        style={styles.input}
        // onChangeText={handleFirstNameChange}
        // value={firstName}
      />
      <Text style={styles.label}>Last Name</Text>
      <TextInput
         style={styles.input}
        // onChangeText={handleLastNameChange}
        // value={lastName}
      />
      <Text style={styles.label}>Telephone</Text>
      <TextInput
         style={styles.input}
        // onChangeText={handleEmailChange}
        // value={email}
        // keyboardType="email-address"
      />
      <Text style={styles.label}>Check-In Date</Text>
      <TextInput
         style={styles.input}
        // onChangeText={handleCheckInDateChange}
        // value={checkInDate}
        // keyboardType="numeric"
      />
      <Text style={styles.label}>Check-Out Date</Text>
      <TextInput
        style={styles.input}
        // onChangeText={handleCheckOutDateChange}
        // value={checkOutDate}
        // keyboardType="numeric"
      />
      <TouchableOpacity>
      <Button title="Submit" style={styles.button} />
      </TouchableOpacity>
    </View>
            
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
   container: {
    
    marginHorizontal: 20,
    marginTop:27
   },
  label: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    marginBottom: 20,
    borderRadius: 5,
    width: '100%',
    fontSize: 25,
    padding: 10,
    marginBottom: 30,
    borderBottomWidth: 0.5,
    borderBottomColor: 'green',
    marginTop:10
  },
  header: {
    marginTop: 25,
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
  },
  label:{
    textAlign:'center',
    color:COLORS.primary
  },

  button:{
    // height: 55,
    // justifyContent: 'center',
    // alignItems: 'center',
    marginTop: 40,
  Color: COLORS.primary,
    marginHorizontal: 20,
    borderRadius: 10,
  }
});

export default AddReservationScreen;
