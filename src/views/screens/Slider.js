import React, { useState } from 'react';
import { StyleSheet, View, Image, Dimensions, ScrollView } from 'react-native';

const { width } = Dimensions.get('window');

const Slider = props => {
  const { images } = props;
  const [active, setActive] = useState(0);

  const change = ({ nativeEvent }) => {
    const slide = Math.ceil(
      nativeEvent.contentOffset.x / nativeEvent.layoutMeasurement.width,
    );
    if (slide !== active) {
      setActive(slide);
    }
  };

  return (
    <View style={styles.container}>
      <ScrollView
        pagingEnabled
        horizontal
        onScroll={change}
        showsHorizontalScrollIndicator={false}>
        {images.map((image, index) => (
          <Image key={index} source={{ uri: image }} style={styles.image} />
        ))}
      </ScrollView>
      <View style={styles.pagination}>
        {images.map((i, k) => (
          <View
            key={k}
            style={
              k === active ? styles.activeDot : styles.dot
            }></View>
        ))}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginTop: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  image: {
    width: width,
    height: 250,
  },
  pagination: {
    flexDirection: 'row',
    position: 'absolute',
    bottom: 0,
    alignSelf: 'center',
    padding: 5,
  },
  dot: {
    backgroundColor: '#FFF',
    margin: 3,
    width: 10,
    height: 10,
    borderRadius: 5,
  },
  activeDot: {
    backgroundColor: '#000',
    margin: 3,
    width: 10,
    height: 10,
    borderRadius: 5,
  },
});

export default Slider;
